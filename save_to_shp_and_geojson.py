'''
This python module is used to clear features such as combobox and QLineEditor
'''
import geopandas
import processing
from qgis.core import QgsVectorLayer

def create_strip_shapefile(filepath,field_to_keep,filename,data_path):
    '''
    This function create a new shapefile using split features by charcater
    # layer_cols: layer list of column id name
    # filepath  : the filepath of the data to strip to create new shp file
    # filename  : same as the original filepath
    # data_path : shp file directory same as the original one
    '''
    # Layer reading from source file
    layer = QgsVectorLayer(filepath, ' ') 
    # read all the column id for the original data
    original_columns =layer.fields().names()
    # print('original data: ',original_columns)
    # print('user non cleaned field names: ',field_to_keep)
    clean_field_to_keep = field_to_keep[:-2]

    try: 
        # Check if column value is 'NONE'
        if 'NONE' in clean_field_to_keep:
            clean_field_to_keep.remove('NONE') 
    except:
        pass
    # define the list of layer column to be removed
    columns_to_delete=list(set(clean_field_to_keep).symmetric_difference(original_columns))
    # define the new file name
    outfile = str(data_path)+'\\'+str(filename)+'.shp'
    parameter_for_extract= {'INPUT':str(filepath),'COLUMN':columns_to_delete ,'OUTPUT':outfile}
    output=processing.run('native:deletecolumn', parameter_for_extract)
    return outfile #print(str(filename)+'_strip.shp shapefile created') 
    


def create_geojson_file(outfile,filename,data_path):
    '''
    This function create a geojson file using:
    # filepath : the filepath of the data to save as geojson
    # filename : same as the original filepath
    # data_path: geojson directory
    '''    
    # Now create the geojson file
    myshpfile = geopandas.read_file(outfile)
    myshpfile.to_file(str(data_path)+'\\'+str(filename)+'.geojson', driver='GeoJSON')
    return #print(str(filename)+'.geojson geojson completed')
 

