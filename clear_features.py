'''
This python module is used to clear features such as combobox and QLineEditor
'''
from qgis.core import QgsProject


def clear_all_label(self):
    '''
    This function clear the label associated with ComboBox, as well as the label associated to extra QLineEditor.
    '''
    self.label_list       = [self.moving_Label_1,self.moving_Label_2,self.moving_Label_3,self.moving_Label_4,self.moving_Label_5,self.moving_Label_6,self.moving_Label_7,self.moving_Label_8,self.moving_Label_9,self.moving_Label_10]
    for i in range(len(self.label_list)):
        self.label_list[i].clear()
    self.Intrusion_Label.clear()
    self.Sill_Label.clear()
    


def clear_partially_combo_list(self,break_id,flag):
    '''
    This function clear out partially in a reversed way a combobox list after it is used.
    :flag =1: clear all.
    :flag!=2: clear few and break by the value selected.
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


def hide_all_combo_list(self,flag):
    '''
    This function hide all unnecessary combo elt and label. 
    # flag: value(str) to make the activation selection
    '''
    self.my_combo_list =combo_list(self)
    if flag==0:
        for i in range(len(self.my_combo_list )):
            self.my_combo_list[i].hide() 
        self.Sill_LineEditor.hide()
        self.Intrusion_LineEditor.hide()
        self.Verbose1_radioButton.hide()
        self.Verbose2_radioButton.hide()
        self.Verbose3_radioButton.hide()
        self.Overwrite_checkBox.hide()
        #self.Save_pushButton.hide()
        #self.Saveconfig_pushButton.hide()
        #self.Map2Loop_Button.hide()
        #self.LoopStructural_Button.hide()
    else:
        for i in range(len(self.my_combo_list )):
            self.my_combo_list[i].setVisible(True) 
        self.Sill_LineEditor.setVisible(True)
        self.Intrusion_LineEditor.setVisible(True)
        # self.Verbose1_radioButton.setVisible(True)
        # self.Verbose2_radioButton.setVisible(True)
        # self.Verbose3_radioButton.setVisible(True)
        # self.Overwrite_checkBox.setVisible(True)
        # self.Save_pushButton.setVisible(True)
        # self.Saveconfig_pushButton.setVisible(True)
        # self.Map2Loop_Button.setVisible(True)
        # self.LoopStructural_Button.setVisible(True)
    return 


def hide_dtm_feature(self, dtm_flag):
    '''
    This function activate or desactivate the feature associated to the plugin layer loader options.
    # dtm_flag: value (int) to setEnabled to False and True the various checkbox.
    '''
    load_features =[self.File_checkBox,self.Aus_checkBox,self.Http_checkBox,self.Qgis_checkBox,self.Qgis_comboBox,self.Ok_pushButton]
    LL =len(load_features)

    if dtm_flag ==0:
        for i in range(LL):
            load_features[i].hide()
            
    elif dtm_flag ==1:
        for i in range(LL):
            load_features[i].setVisible(True)

    elif dtm_flag ==2:
        for i in range(LL):
            load_features[i].setEnabled(False) 

    elif dtm_flag ==3:
        self.File_checkBox.setEnabled(False) 
        self.Http_checkBox.setEnabled(False) 
        self.Qgis_checkBox.setEnabled(False)
        self.Qgis_comboBox.setEnabled(False) 
        self.Ok_pushButton.setEnabled(False)

    elif dtm_flag ==4:
        self.File_checkBox.setEnabled(False) 
        self.Aus_checkBox.setEnabled(False) 
        self.Qgis_checkBox.setEnabled(False) 
        self.Qgis_comboBox.setEnabled(False)
        self.Ok_pushButton.setEnabled(False)

    elif dtm_flag ==5:
        self.File_checkBox.setEnabled(False) 
        self.Aus_checkBox.setEnabled(False) 
        self.Http_checkBox.setEnabled(False)
        self.Qgis_comboBox.setVisible(True)
        self.Ok_pushButton.setVisible(True)

    elif dtm_flag==6:                    
        self.Http_checkBox.setEnabled(True)
        self.File_checkBox.setEnabled(True) 
        self.Aus_checkBox.setEnabled(True) 
        self.Qgis_checkBox.setEnabled(False) 
        self.Qgis_checkBox.setCheckable(False)
        self.Qgis_comboBox.setEnabled(False)
        self.Ok_pushButton.setEnabled(False) 

    elif dtm_flag==7:
        for i in range(LL-2):
            load_features[i].setCheckable(True)
            
    elif dtm_flag==8:
        for i in range(LL-2):
            load_features[i].setCheckable(False)  
    elif dtm_flag==9:                       
        self.Http_checkBox.setEnabled(False)
        self.File_checkBox.setEnabled(True) 
        self.Aus_checkBox.setEnabled(False) 
        self.Qgis_checkBox.setEnabled(False) 
        self.Qgis_checkBox.setCheckable(False)
        self.Qgis_comboBox.setEnabled(False)
        self.Ok_pushButton.setEnabled(False) 
    else:
        pass

    return


def reset_qgis_cbox(self,flag):
    '''
    This function is used to reset the various features when Qgis is chosen to load from a layer panel of QGIS.
    # flag=2: to only enable 2 checkbox
    # flag=4: to enable all the 4 checkbox
    '''
    if flag==2:
        self.Qgis_comboBox.clear()
        self.File_checkBox.setChecked(False)
        self.Qgis_checkBox.setChecked(False)
        self.File_checkBox.setEnabled(True)
        self.Qgis_checkBox.setEnabled(True)
    elif flag==4:
        self.Qgis_comboBox.clear()
        self.Http_checkBox.setEnabled(True)
        self.Http_checkBox.setCheckable(True)

        self.File_checkBox.setEnabled(True)
        self.File_checkBox.setCheckable(True)

        self.Aus_checkBox.setEnabled(True) 
        self.Aus_checkBox.setCheckable(True)

        self.Qgis_checkBox.setEnabled(True) 
        self.Qgis_checkBox.setCheckable(True)

        self.Qgis_comboBox.setEnabled(True)
        self.Ok_pushButton.setEnabled(True)
    else:
        pass

    return


def hide_http(self,flag):
    '''
    This function is used to reset the text editor features when Http is chosen to load your own server addres.
    # flag=0: to hide all the features such as textlabel, qtexeditor and save button
    # flag !=0: to enable all the 3 features above
    '''
    http_features =[self.Http_Label,self.Http_TextEdit, self.SaveHttp_pushButton]
    LH = len(http_features)
    
    if flag==0:
        for i in range(LH):
            http_features[i].hide()
    else:
        for i in range(LH):
            http_features[i].setVisible(True)
            if i==0:
                http_features[i].move(131,140)
            elif i==1:
                self.Http_TextEdit.clear()
                http_features[i].move(131,160)
            elif i==2:
                http_features[i].move(541,190)
            else:
                pass
           
    return


def disabled_qgis_chkbox(self):
    '''
    This function setEnabled(False) for qgis chkbox option to False when no layer is available on the qgis main layer panel.
    '''
    if not QgsProject.instance().mapLayers().values() : 
        self.Qgis_checkBox.setEnabled(False)
    return


def retry_function(self,label):
    '''
    After the data are uploaded using our plugin qgis option:
    Once Retry function is activated, this function clear and hide all combo box when dtm is reloaded.
    # label: In this case it is <Save Config File> qt feature
    '''
    try:

        if label=='Saveconfig_pushButton':
            hide_all_combo_list(self,0) 
    except:
        pass 

    return

