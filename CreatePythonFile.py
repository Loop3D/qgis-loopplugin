#Michel Nzikou @UWA-MinEx CRC Perth, October 2022
####This function  create a python file whith the below data:
# file_path  --> this is the file path
# pyfilename --> is the name of the saved files
# data1      --> is the project creation data
# data2      --> is the project file configuration
# data3      --> is the project run command
# data4      --> is use to copy qgz file into a different directory
#from PyQt5.QtWidgets import QMessageBox
def create_a_python_file(file_path,pyfilename, Module_Import,data1,data2,data3,data4):
	file = open(str(file_path+'/'+pyfilename)+'.py', 'w')
	file.write(Module_Import+data1+data2+data3+data4)
	file.close()
	return 
#############################################################################################################

