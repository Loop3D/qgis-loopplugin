'''  
Michel Nzikou @UWA-MinEx CRC Perth, October 2022
This function load vector layers into the Qgis framework
'''

import os 
#from qgis.core import QgsProject
import glob
from qgis.utils import iface
import json
import io
from PyQt5.QtWidgets import QMessageBox


def shape_file_loader(file_list):
    '''
    This function load Layers from the directory folder after it is selected.
    '''
    for path_to_vector_layer in file_list:
        fn_path    = str(path_to_vector_layer)
        layer_name =str(fn_path.split('/')[-1].split('.')[0])
        ext=str(fn_path.split('.')[-1])
        if ext=='tif':
            vlayer = iface.addRasterLayer(fn_path,layer_name)
        else:
            vlayer = iface.addVectorLayer(fn_path,layer_name, "ogr")
    return 


def xlayer_reader():
    '''
    This function return the list of column name of a layer table.
    '''
    mc = iface.mapCanvas()
    lyr= mc.currentLayer()
    layer_colnames = [ ]
    for field in lyr.fields():
      layer_colnames.append(field.name())
    return layer_colnames


def create_json_file(data_path,data):
    '''
    This function create json file to your given directory.
    : data_path: json file path
    : data: data to be written into the json file
    '''
    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str
    with io.open(str(data_path)+'/'+'data.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(data,indent=4,sort_keys=True, separators=(',',':'),ensure_ascii=False)
        outfile.write(to_unicode(str_))
        return

