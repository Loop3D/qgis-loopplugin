import json
from PyQt5.QtWidgets import QCheckBox, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox
'''
This module save parameters into json and also use it to load it in the front-end
'''

def save_param_to_json(data,file_path):
	# data     : Define the dictionary
	# file_path: the folder to save the data
	# Save the dictionary as a JSON file
	file_path = str(file_path)+'/load_data.json'
	with open(file_path, 'w') as json_file:
		json.dump(data, json_file,indent=4)

	print(f"Dictionary saved as {file_path}")
	return

def select_load_json_file(self):
	'''
	This function filter data to select json ly files
	'''
	try:
		self.select_json_file=QFileDialog.getOpenFileNames(
				self,
				"Filtered file",
				"",
				"Filtered files (*.json* *.JSON*)",
			)
			#shape_file_list.append(shape_file)
		return self.select_json_file[0][0]
	except:
		print('OOPS I cant select the json file')
		return


# Function to read JSON data from a file
def read_json(file_path):
	''' 
	This function load json and create a new variable called data 
	'''
	try:
		with open(file_path, 'r') as file:
			data = json.load(file)
			return data
	except FileNotFoundError:
		print(f"File {file_path} not found.")
	except json.JSONDecodeError:
		print(f"Error decoding JSON from {file_path}.")
	except Exception as e:
		print(f"An error occurred: {e}")


# Function to iterate through the keys and values
def print_keys_values(data, flag):
	''' 
	This function load json string, convert it to dict and extract (key, pair) 
	'''
	#print(flag)
	# convert string into dictionary
	data = json.loads(data)
	#print(data)
	if flag=='Geology':
		geo_par = data['geol_head']
		geo_col = data['geology column']
		geo_path= data["geol_path"]
		dtm_path= data["dtm_path"]
		csv_path    = data["csv_path"]
		hjson_path  = data["hjson_path"]
		return geo_par,geo_col,geo_path,dtm_path,csv_path,hjson_path
	elif flag=='Fault':
		fault_par = data['fault_head']
		fault_col = data['fault column']
		fault_path= data["fault_path"]
		dtm_path= data["dtm_path"]
		csv_path    = data["csv_path"]
		hjson_path  = data["hjson_path"]
		return fault_par,fault_col,fault_path,dtm_path,csv_path,hjson_path
	elif flag=='Structure':
		struct_par  = data['struct_head']
		struct_col  = data['structure column']
		struct_path = data["struct_path"]
		dtm_path    = data["dtm_path"]
		csv_path    = data["csv_path"]
		hjson_path  = data["hjson_path"]
		return struct_par,struct_col,struct_path, dtm_path,csv_path,hjson_path

         
	return
