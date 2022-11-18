'''
This python module is used to clear features such as combobox and QLineEditor
'''

def clear_all_label(self):
    '''
    This function clear the label associated with ComboBox, as well as the label associated to extra QLineEditor.
    '''
    for i in range(len(self.label_list)):
        self.label_list[i].clear()
    self.Intrusion_Label.clear()
    self.Sill_Label.clear()


def clear_partially_combo_list(self,break_id,flag):
        '''
        This function clear out partially in a reversed way a combobox list after it is used.
        :flag =1: clear all.
        :flag!=1: clear few and break by the value selected.
        '''
        for i in reversed(range(10)):
            if flag==1:  
                self.my_combo_list[i].clear() 
            else:
                self.my_combo_list[i].hide() 
            if i==break_id:
                break


def combo_list(self):
    '''
    This function return a list combo elt . 
    '''
    self.my_combo_list =[self.cmbFormationLayerIDName,self.cmbGroupLayerIDName,
                        self.cmbSupergroupLayerIDName,self.cmbDescriptionLayerIDName,
                        self.cmbFmLayerIDName, self.cmbRocktype1LayerIDName,
                        self.cmbRocktype2LayerIDName,self.cmbPointIDLayerIDName,
                        self.cmbMinAgeLayerIDName,self.cmbMaxAgeLayerIDName] 
    return self.my_combo_list


