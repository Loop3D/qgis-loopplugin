"""
Michel Nzikou @UWA-MinEx CRC Perth, October 2022
"""

from PyQt5.QtWidgets import QMessageBox


def save_a_python_file(
    self, file_path, pyfilename, Module_Import, data1, data2, data3, data4
):
    """
    This function  create a python file whith the below data:
    file_path  --> this is the file path
    pyfilename --> is the name of the saved files
    data1      --> is the project creation data
    data2      --> is the project file configuration
    data3      --> is the project run command
    data4      --> is use to copy qgz file into a different directory
    """
    try:
        file = open(str(file_path + "/" + pyfilename) + ".py", "w")
        file.write(Module_Import + data1 + data2 + data3 + data4)
        file.close()
    except:
        QMessageBox.about(
            self, "File Configuration Status", "* Python File Not created *"
        )

    return


def find_relative_path(self, label, DTM_filename):
    """
    This function use as input parameter "filename" and flag to find its absolute path.It uses
    "os.path.dirname()" to get the directory name and "os.path.join()"
    to join the directory name and the filename to form the absolute path whic is then
    returns a the absolute path or the relative path.
    # DTM_filename: file path of the layer selected
    """
    if label == "Aus_checkBox" or label == "Http_checkBox":
        filename = str(DTM_filename)
    elif label == "Qgis_checkBox" or label == "File_checkBox":
        dtm_list = str(DTM_filename).split("/")
        # dtm_length   = len(dtm_list)
        dtm_rel_path = "..\\" + "\\".join(dtm_list[-3:])
        filename = dtm_rel_path
    else:
        pass
    return filename
