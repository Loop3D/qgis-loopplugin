'''
Michel Nzikou @UWA-MinEx CRC Perth, February 15, 2023
This python module create:
    1- a polygon or region of interest shape file which is saved in your data directory 
    2- then new layer is created by clipping the roi into the bigger layer, with overlay=roi.
    3- the output layer have the size of roi with data from the input layer
    4- the output layer directory is in the same as the input layer
'''

import os
import glob
from pathlib import Path
from qgis.core import *
import processing
from qgis.utils import iface
from qgis.core import QgsProject,QgsVectorLayer,QgsVectorFileWriter,QgsCoordinateTransformContext
from qgis.core import QgsRasterLayer
from PyQt5.QtWidgets import QMessageBox
from .feature_import import welcoming_image
#set input and output file names


def create_scratch_layer(self,flag):
    '''
    This function create  a scratch layer depending on the type of layer to ROI
    # flag =0: to create a polygon temp layer, 
    # flag =1: to create a point temp layer
    '''  
    if flag==0:     # Fault and geology layer
        layer_type ='Polygon?'
    elif flag==1:   # Structure point or point layer 
        layer_type ='Polygon?'  
    else:
        pass
    welcoming_image(self,2)
    
    ## While this section deal with layer available in Qgis layer panel
    layers_list     = QgsProject.instance().mapLayers().values()
    layer_paths     = [layer.dataProvider().dataSourceUri() for layer in layers_list]
    part_path       = Path(str(layer_paths[0])).parts
    self.clip_path  = 'C:/'+"/".join(part_path [1:len(part_path )-1])

    new_layer =  QgsVectorLayer(str(layer_type), 'temp_layer' , "memory")  #
    QgsProject.instance().addMapLayers([new_layer])
    new_layer.startEditing()
    options = QgsVectorFileWriter.SaveVectorOptions()
    options.driverName = "ESRI Shapefile"
    QMessageBox.about(self,"ROI selection", "Draw your ROI")
    self.draw_your_ROI=True #QMessageBox.question(self,"ROI selection", "Draw your ROI",QMessageBox.Yes)
    set_your_clip(self,140, 140)
    
    return self.clip_path


def saving_your_roi(new_layer,layerpath):
    '''
    This code create new temp layer <roi.shp> from scratch layer <temp_layer> in the above function. 
    Then, the roi clip is clipped to your early selected layer to create a new layer with the following name: <your_selected_layername_clip.shp>.
    # new_layer: new_scratch layer
    # layerpath: absolute path of the new_layer 
    # Create a ROI layer for future use for other layer into the project
    '''
    
    roi_clip   = str(layerpath)+"/roi.shp"
    try:
        if str(new_layer.name()) =='temp_layer':
            new_layer.startEditing()
            options = QgsVectorFileWriter.SaveVectorOptions()
            options.driverName = "ESRI Shapefile"
            QgsVectorFileWriter.writeAsVectorFormatV2(new_layer,roi_clip,QgsCoordinateTransformContext(), options)
            iface.addVectorLayer(roi_clip, '', 'ogr')
    except:
        pass
    return 


def select_your_roi_region(self,new_layer,flag):
    '''
    This code create new temp layer <roi.shp> from scratch layer <temp_layer> in the above function. 
    Then, the roi clip is clipped to your early selected layer to create a new layer with the following name: <your_selected_layername_clip.shp>.
    # new_layer: new_scratch layer
    # layerpath: absolute path of the new_layer
    # flag     : 1 for structure point layer,
    # flag     : 5 for fault polyline,  
    # flag     : 6 for geology polygon, 
    '''
    try:
        # This section define path for input and output layers 
        out        = new_layer.dataProvider().dataSourceUri()
        out        = Path(str(out)).parts
        name_out   = out[-1].split('.')[0]
        extension  = out[-1].split('.')[-1]
        join_path  = out[0]+"/".join(out[1:len(out)-1])
        out_path   = join_path+'/'+name_out+'_clip.'+str(extension)

        # Create a layer for the feature and add to the project
        layers     = [tree_layer.layer() for tree_layer in QgsProject.instance().layerTreeRoot().findLayers()]
        roi_layer  = [a for a in layers if a.name()=='roi'][0]
        if flag ==1:  # struct and dtm layer condition
            if type(new_layer).__name__=='QgsVectorLayer':
                struct_path= str(new_layer.dataProvider().dataSourceUri())
                roi_path   = str(roi_layer.dataProvider().dataSourceUri())
                processing.run("native:clip", {'INPUT': struct_path,
                                                'OVERLAY':roi_path,
                                                'OUTPUT':out_path })
                iface.addVectorLayer(out_path, name_out+'_clip', 'ogr')

            else:
                output_layer=clipping_dtm(new_layer, roi_layer)
                # Save the data in your project directory
                QgsVectorFileWriter.writeAsVectorFormat(output_layer,out_path ,"UTF-8", output_layer.crs(), "ESRI Shapefile")
            
        elif flag==5 or flag==6:   # geology and fault condition
            layer_to_clip = str(new_layer.dataProvider().dataSourceUri())
            roi_path      = str(roi_layer.dataProvider().dataSourceUri())
            if type(new_layer).__name__=='QgsVectorLayer':
                # This works for fault polyline (flag=5) and geology polygon (flag=6)
                processing.run("native:clip", { 
                                                        'INPUT': layer_to_clip,
                                                        'OUTPUT':out_path,
                                                        'OVERLAY':roi_path,})
                iface.addVectorLayer(out_path, name_out+'_clip', 'ogr') 

            else:
                pass
        else:
            pass
    except:
        pass

    try:
        # this is used to add the dtm into qgis panel
        if type(new_layer).__name__=='QgsRasterLayer':
            for x in glob.glob(str(join_path)+'/*.tif', recursive=True):
                if '_clip' in x:
                    rlayer = QgsRasterLayer(str(x), str(name_out)+'_clip')
                    if not rlayer.isValid():
                        print("Layer failed to load!")
                    else:
                        QgsProject.instance().addMapLayer(rlayer)
        else:
            pass

    except:
        pass
    try:
        # this is used to remove output layer from the temporary files
        remove_me     = [x for x in layers  if x.name() == 'output'][0]
        check_if_roi_exist(remove_me.id())
    except:
          pass
    
    self.Ok_ClipLayer.hide()
    return 



def check_if_roi_exist(layer_to_remove):
    '''
    This function check if temp_layer exist in Qgis layer panel
    # layer_to_remove: Layer to remove from the qgis panel
    '''

    layers_list      = QgsProject.instance().mapLayers().values()
    names            = [layer.name() for layer in layers_list]
    for name in names:
        if str(name) =='output' or str(name)=='temp_layer':
             QgsProject.instance().removeMapLayers( [layer_to_remove] )
        else:
            pass
    return


def clipping_dtm(layer_1, layer_2):
    '''
    This function is used to clip dtm layer from drawn or existing roi layer
    '''  
    out        = layer_1.dataProvider().dataSourceUri()
    out        = Path(str(out)).parts
    name_out   = out[-1].split('.')[0]
    extension  = out[-1].split('.')[-1]
    join_path  = out[0]+"/".join(out[1:len(out)-1])
    out_path   = join_path+'/'+name_out+'_clip.'+str(extension) 
    layer_clip =processing.run("gdal:cliprasterbymasklayer", {'INPUT':layer_1,'MASK':layer_2,'SOURCE_CRS':None,
                                                                  'TARGET_CRS':None,'TARGET_EXTENT':None,'NODATA':None,
                                                                  'ALPHA_BAND':False,'CROP_TO_CUTLINE':False,'KEEP_RESOLUTION':True,
                                                                  'SET_RESOLUTION':False,'X_RESOLUTION':None,'Y_RESOLUTION':None,  
                                                                  'MULTITHREADING':False,'OPTIONS':'','DATA_TYPE':0,'EXTRA':'','OUTPUT':out_path})["OUTPUT"] 
    QgsProject.instance().addMapLayer(layer_clip)
    return layer_clip



def set_your_clip(self,x,y):
    '''
    This is the set style for clipper function button
    # x: x-position value
    # y: y-position value
    '''

    self.Ok_ClipLayer.setVisible(True)
    self.Ok_ClipLayer.setStyleSheet("background-color: rgb(97, 97, 97);" 
                                    "border-style: double;" "border-width: 3px;" 
                                    "border-color: rgb(100, 100, 100);" "border-radius: 4px;"
                                    "color:rgb(255, 255, 255);")
        

    self.Ok_ClipLayer.setStyleSheet( "border :5px solid; " "border-top-color : red; "
          "border-left-color :pink;"
          "border-right-color :yellow;"
          "border-bottom-color : green")

    self.Ok_ClipLayer.move(x,y)
    return

