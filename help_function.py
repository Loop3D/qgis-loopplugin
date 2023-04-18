'''
Michel Nzikou @UWA-MinEx CRC Perth, October 2022
This function  create a help dictionary library:
'''
import os
import json

#
BASE_DIR           = os.path.dirname(__file__)
help_config_path   = str(BASE_DIR)+'/help_config.json'



def welcome_msg():
    '''
    This welcome_msg is used to guide the user on how to use the plugin.
    '''   
    startup_msg = { welcome_msg:":::::::::::: Welcome to Loop Processor v0.3 ::::::::::::\n \n Below is your user guideline infos: \n \n\n\n 1--> Define your Project Directory \n \n 2--> Load data by clicking: \n \n   ** Geology \n \n   ** Fault  \n \n   ** Structure  \n \n   ** DTM  \n \n   Note that the click order is not important. \n \n 3--> Save Config File \n \n 4--> Run map2loop \n \n 5--> View map2loop outputs \n \n 6--> Run LoopStructural"
                  } 
    return startup_msg[welcome_msg]
        
        
def layer_msg(layer):       
    '''
    This is used to guide the user on how to load the geol layer.
    # Qgis: Select from qgis layer panel
    # Aus : Automatically select the GA webserver portal
    # File: Let you select your dtm file from any folder
    # Http: Let you select your webserver portal

    '''
    if layer=='DTMButton':
        layer_help = {layer_msg: "Load your raster layer using the below options: \n \n\n\n 1--> Qgis: From loaded layers of qgis layer panel \n\n 2--> Aus : From Goescience Australia server \n \n 3--> File:   From any folder into your local machine \n \n 4--> Http: From  your own webserver portal"
                     }
    else:
        layer_help=  {layer_msg: "Load your vector layer using the below options: \n \n\n\n 1--> Qgis: From loaded layers of qgis layer panel \n \n 2--> File:   From any folder into your local machine"
                     }
    return  layer_help[layer_msg]


def save_config_msg():       
    '''
    This is used to guide the user on how to save and create the configuration file.
    '''
    config_help= {save_config_msg: "Create your python and json config file with the below options: \n \n\n\n 1--> If not loaded, select the source path \n\n 2--> Click <Save Config File>"
                 }
    return config_help[save_config_msg]


def retry_msg():       
    '''
    This is used to guide the user on how to save and create the configuration file.
    '''
    retry_help= {retry_msg: "  \n \n\n\n  \n \n\n\n  \n \n\n\n  All Features have been reset. \n \n Load your data! "
                }
    return retry_help[retry_msg]


def folder_msg():       
    '''
    This show the loading project folder path.
    '''
    load_project_folder= {folder_msg: "  \n\n Loading the project folder path........> "
                }
    return load_project_folder[folder_msg]


def sort_layer_param(col_list,id,layerobjectName):
    '''
    This function look for existing layer parameter from the help_config file.
    If the given layer column ID exist in the help config param, then it is pushed upfront of the list
    '''
    # Here we define the info that are attached to the layer associated to individual Qpush button such as:
    # Geol...>[Formation*,Group, Supergroup, Description, Fm code, Rocktype 1, Rocktype 2, Polygon ID, Min Age, Max Age ] 
    # uniqueID[]
    with open(help_config_path) as complex_data:
        data = json.load(complex_data)

    if layerobjectName=='StructButton':
        col_of_interest=struct_sorter(data,id)
    elif layerobjectName=='FaultButton':
        col_of_interest=fault_sorter(data,id)
    elif layerobjectName=='GeolButton':
        col_of_interest=geol_sorter(data,id)
    else:
         pass
    ncol_list=compare_two_list(col_list,col_of_interest)    
    return ncol_list

      

def compare_two_list(list1,list2):
    '''
    This code compare two lists and return sorted list based on common element
    id: is the index of the first combobox elet
    list1: column to be sorted
    list2: column of the data base in which we match for common element
    '''
    try:
        list_ref=[]
        for idx,col_elt in enumerate(list1):
            for col_dir_params in list2:
                
                if col_elt.lower()==col_dir_params.lower():           
                    list1.insert(0,list1.pop(idx))
                    list_ref.append(list1)
                break
        sorted_list=list_ref[0]
    except:
        sorted_list=list1 
    return sorted_list


def struct_sorter(data,id):
    '''
    This code sort layer data so that the best selection of the variable is printed nbre 1 on combobbox view
    # data: layer data to show in the table widget
    # id: combobox index id to be filled by the sorted columns name
    '''
    col_of_interest1 =[]
    col_of_interest2 =[]
    for majorkey in data:
        if majorkey=='Orientations_dictionary':
            if '_params' in str(data[majorkey].keys()):
                col_of_interest1=[a for a in data[majorkey].values() if type(a) is list][0:4]
        if majorkey=='ids_dictionary':
            col_of_interest2.append([a for a in data[majorkey].values() if type(a) is list][0])
        col_of_interest=col_of_interest1+col_of_interest2
    if id==0:
        col_of_interest=col_of_interest[0]  
    elif id==1:
        col_of_interest=col_of_interest[1] 
    elif id==2:
        col_of_interest=col_of_interest[2]     
    elif id==4:
        col_of_interest=col_of_interest[3]    
    elif id==5:
        col_of_interest=col_of_interest[4]
    else:
        pass 
   
    return col_of_interest


def fault_sorter(data,id):
    '''
    This code sort layer data so that the best selection of the variable is printed nbre 1 on combobbox view
    # data: layer data to show in the table widget
    # id: combobox index id to be filled by the sorted columns name
    '''
    col_of_interest1=[]
    col_of_interest2=[]
    for majorkey in data:
        
        if majorkey=='Fault_and_folds':
            if '_params' in str(data[majorkey].keys()):
                col_of_interest1=[a for a in data[majorkey].values() if type(a) is list][2:]
        elif majorkey=='ids_dictionary': 
             col_of_interest2.append([a for a in data[majorkey].values() if type(a) is list][0]) 
        col_of_interest=col_of_interest1+col_of_interest2
    if id==0:
        col_of_interest=col_of_interest[0]  
    elif id==1:
        col_of_interest=col_of_interest[1] 
    elif id==2:
        col_of_interest=col_of_interest[2]     
    elif id==4:
        col_of_interest=col_of_interest[3]    
    elif id==5:
          col_of_interest =col_of_interest[4]
    else:
        pass 

    return col_of_interest


def geol_sorter(data,id):
    '''
    This code sort layer data so that the best selection of the variable is printed nbre 1 on combobbox view
    # data: layer data to show in the table widget
    # id: combobox index id to be filled by the sorted columns name
    '''
    col_of_interest1=[]
    col_of_interest2=[]
    col_of_interest3=[]
    for majorkey in data:  
        if majorkey=='stratigraphy_dictionary':
            if '_params' in str(data[majorkey].keys()):
                col_of_interest1=[a for a in data[majorkey].values() if type(a) is list][:7]
                
        elif majorkey=='ids_dictionary': 
             col_of_interest2.append([a for a in data[majorkey].values() if type(a) is list][0]) 
        elif majorkey=='timing':
            if '_params' in str(data[majorkey].keys()):
                col_of_interest3=[a for a in data[majorkey].values() if type(a) is list]
        col_of_interest=col_of_interest1+col_of_interest2+col_of_interest3
    for idx in range(9):
        if id==idx:
           col_of_interest=col_of_interest[idx]

    return col_of_interest