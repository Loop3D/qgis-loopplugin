import json
from PyQt5.QtWidgets import QCheckBox, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import Qt
'''
This module save parameters into json and also use it to load it in the front-end
'''

def json_combbox_activate(self,list_cbbox, data):
	''' 
	This function activate ccombobox and its labels
	'''
	# Activate all
	for cbbox_feature in list_cbbox:
		print(cbbox_feature)
		cbbox_feature.setVisible(True)
	print('Success')
	return 

def data_from_json_to_cbbox(self,list_cbbox, data,col_data):
	'''
	This function use json dictionary to append it to main combobox
	data    : param dictionary
	col_data: dolum header dictionary
	'''	 
	key_pair = data.items()
	for idx,(key, val) in enumerate(key_pair):
		list_cbbox[idx].addItems([val])
		if idx== len(list_cbbox)-1:
			self.GeolButton.setEnabled(False)
			self.Geology_checkBox.setChecked(True)
			self.FaultButton.setEnabled(True)
			break

	return

 