#Michel Nzikou @UWA-MinEx CRC Perth, October 2022
## This function is needed to load vector layers
import os # This is is needed in the pyqgis console also
from qgis.core import QgsVectorLayer
from qgis.core import QgsProject
import glob
from qgis.utils import iface
import json
import io
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QComboBox,QLabel,QAction, QFileDialog, QMessageBox, QTreeWidgetItem
from qgis.gui import QgsMapToolEmitPoint, QgsRubberBand
##########################################################
###### This function load Layers into a scroll down search
def shapeFileloader(file_list):
    for path_to_vector_layer in file_list:
        fn_path    = str(path_to_vector_layer)
        layer_name =str(fn_path.split('/')[-1].split('.')[0])
        ext=str(fn_path.split('.')[-1])
        if ext=='tif':
            vlayer = iface.addRasterLayer(fn_path,layer_name)
        else:
            vlayer = iface.addVectorLayer(fn_path,layer_name, "ogr")
    return 
###### This function generate Layer ID or it's column name 
def xLayerReader():
    mc = iface.mapCanvas()
    lyr= mc.currentLayer()
    #print('', lyr.name())
    #print('The active layer name is {}'.format(lyr.name()))
    layer_colnames = [ ]
    for field in lyr.fields():
      layer_colnames.append(field.name())
    #print('The active col name is {}'.format(layer_colnames))
    return layer_colnames
###### This function create json file     
def create_json_file(data_path,data):
    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str
    with io.open(str(data_path)+'/'+'data.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(data,indent=4,sort_keys=True, separators=(',',':'),ensure_ascii=False)
        outfile.write(to_unicode(str_))
        return
#####################################

def evaluatePipeLine(self, point, button):
    if button ==Qt.LeftButton:
        self.rbPipeLine.addPoint(point)
        self.rbPipeLine.show()
    elif button == Qt.RightButton:
        pipeline = self.rbPipeLine.asGeometry()
        QMessageBox.information(None,"Pipeline",pipeline.asWkt())
        self.rbPipeLine.reset()

    ############################################################################################################
def RemoveAllLayersExcept(label1,label2):
    # This function remove the existing layer
    if label1.isEnabled() and label2.isChecked():
        #QgsProject.instance().removeMapLayer(lyr)
        List_of_layers=QgsProject.instance().mapLayers()
        for idx,lyr in enumerate(List_of_layers):
            #    #lyr = List_of_layers[i]
            QgsProject.instance().removeMapLayer(lyr)
            if idx==0:
               break

    return
    # layer_ids = []
    # for l in layers:
    #     layer_ids.append(l.id())
    # print('layer_ids', layer_ids)
    # for lyr in QgsProject.instance().mapLayers():
    #     print(lyr)
    #     if lyr not in layer_ids:
    #         print('not')
    #         #QgsProject.instance().removeMapLayer(lyr)
    #     else:
    #         pass