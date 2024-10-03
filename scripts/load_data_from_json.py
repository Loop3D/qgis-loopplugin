import json
from PyQt5.QtWidgets import QCheckBox, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import Qt
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

# Function to handle checkbox state change
def json_loader():

    print ('Json is checked')
    #print(Qt.Checked)

    return