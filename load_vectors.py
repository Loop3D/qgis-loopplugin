'''  
Michel Nzikou @UWA-MinEx CRC Perth, October 2022
This function load vector layers into the Qgis framework
'''

import os 
import glob
from qgis.utils import iface
import json
import io
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
from qgis.PyQt import QtWidgets


def shape_file_loader(file_list):
    '''
    This function let you load layers from any directory.
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


def xlayer_reader(self):
    '''
    This function return the columns name as a list for a selected layer.
    It can be loaded manually from your PC or from Qgis layer panel.
    '''
    mc = iface.mapCanvas()
    lyr= mc.currentLayer()

    layer_colnames = [ ]
    for field in lyr.fields():
      layer_colnames.append(field.name())

    lyr =iface.activeLayer()
    cols_header = [f.name() for f in lyr.fields()] 
    data =[ft.attributes() for ft in lyr.getFeatures()]
    #Let show the datatable 
    load_data_table(self,data[0:10], cols_header)
  
    return layer_colnames


def create_json_file(data_path,data):
    '''
    This function create json file to your given directory.
    #data_path: json file path
    #data: data to be written into the json file
    '''
    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str
    with io.open(str(data_path)+'/'+'data.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(data,indent=4,sort_keys=True, separators=(',',':'),ensure_ascii=False)
        outfile.write(to_unicode(str_))
        return



def load_data_table(self,data_array, cols_header):
    '''
    This function is used to append the data into tablewidget 
    #data_array:  data to show in the table widget
    #cols_header: list of columns names for the above data
    '''
    Nbre_Rows =len(data_array)
    Nbre_cols =len(data_array[0])         # For vizualization purpose, we set nbre of rows=10
    self.tableWidget.setRowCount(Nbre_Rows)
    self.tableWidget.setColumnCount(Nbre_cols)
    self.tableWidget.setHorizontalHeaderLabels(cols_header)
    for row,data in enumerate(data_array):
        for id, val in enumerate(data):
           self.tableWidget.setItem(row,id,QtWidgets.QTableWidgetItem(str(val)))
    self.tableWidget.setVisible(True)


def qgis_load_table(self,lyr,colname):
    '''
    This code is used to show the data table of the layer when qgis option.
    lyr:     The select layer in which the data will be shown
    colname: The list of columns ids of the data table
    '''
    data =[ft.attributes() for ft in lyr.getFeatures()]
    load_data_table(self,data[0:10],colname)
    return