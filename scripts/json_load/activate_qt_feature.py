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

def data_from_json_to_cbbox(self,list_cbbox, data,col_data,flag):
	'''
	This function use json dictionary to append it to main combobox
	data    : param dictionary
	col_data: dolum header dictionary
	'''	
	#
	key_pair = data.items()
	for idx,(key, val) in enumerate(key_pair):
		col_data_clean = remove_duplicate(val, col_data)
		list_data = [val]+col_data_clean
		if flag == 'Geology':
			#print(idx, key, val)
			list_cbbox[idx].clear()
			list_cbbox[idx].addItems(list_data)
			if idx== len(list_cbbox)-1:
				self.GeolButton.setEnabled(False)
				self.FaultButton.setEnabled(True)
				break
		elif flag=='Fault':
			#print(idx, key, val)
			list_cbbox[idx].clear()
			list_cbbox[idx].addItems(list_data)
			self.FaultButton.setEnabled(False)
			self.StructButton.setEnabled(True)

		elif flag=='Structure':
			# print(idx, key, val)
			list_cbbox[idx].clear()
			list_cbbox[idx].addItems(list_data)
			self.StructButton.setEnabled(False)
			self.DTMButton.setEnabled(True)
		else:
			print(f"No flag have been selected")

	return


def remove_duplicate(element,my_list):
	'''
    This function search and remove duplicate if it exist!
    element:  Element to search for and remove
    my_list:  the list to search for duplicate
	'''

	# Check if element exists in the list
	if element in my_list:
	    my_list.remove(element)
	    #print(f"{element} removed from the list.")
	else:
		pass
	    #print(f"{element} not found in the list.")

	#print("Updated list:", my_list)
	return my_list
