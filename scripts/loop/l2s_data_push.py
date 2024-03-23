## All loop matters
import os, shutil
import glob
import webbrowser


## loopstructural data manipulation
def push_data_into_l2s_server(m2l_output_data, l2s_source_data):
    """
    This function is used to push data for loopstructural server
    m2l_output_data    : the loop3d filepath inside m2l_output data folder (i.e outpu_data)
    l2s_source_data: the l2s source data (i.e: loopstructural_source_data)
    """
    list_of_files = glob.glob(str(m2l_output_data) + "/*")
    #data_dict {}
    for ext in [".loop3d"]:
        for file in list_of_files:
            #print(f"extension {ext} in file {file}")
            if str(ext) in str(file).lower():
                # Get the file name
                file_name = os.path.basename(file)
                shutil.copyfile(file, str(l2s_source_data) + "/" + str(file_name))
                data_dict={"LPFilename": str(file_name)}
            else:
                pass
    
    return data_dict
    

def  push_processed_into_loopsource_data(source_data_path, loopstructural_source_data):
    '''
    This function is used to push dtm into loopstructural source data folder
    '''
    list_of_files = glob.glob(str(source_data_path) + "/*")
    #for ext in [".tif"]:
    for file in list_of_files:
        file_name = os.path.basename(file)
        #if str(ext) in str(file).lower():
        shutil.copyfile(file, str(loopstructural_source_data) + "/" + str(file_name))
        # else:
        #     pass

    return print('dtm to loop source data transfert:  Success')


def show_3d_plot(url):
    '''
    This function is used to plot 3d model in a browser
    url: html file data
    '''
    # Open the HTML file in the default web browser
    webbrowser.open('file://' + url)

    print(f'Visualizing data from container {url}: Success')
    return