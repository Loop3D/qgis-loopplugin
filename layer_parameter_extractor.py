'''
This python module generate data from individual layers.
This option is activated only when we choose qgis panel as the option to load the layer.

'''
from .feature_import import label_mover,qline_and_label_mover,qlineeditor_default_string
from .clear_features import clear_partially_combo_list,hide_all_combo_list
from .load_vectors   import qgis_load_table



def load_data_when_qgis_is_choosen(self,colname, geol_name,lyr):
    '''
    This function load col name of qgis layer if qgis checkbox is chosen as the data loader option
    # colname  : list of layer column name
    # geol_name: the sender object name, this can be GeolButton, FaultButton and so on...
    # lyr      : the layer in use or layer selected to extract informations
    '''
    self.colNames    = colname
    clear_partially_combo_list(self,10,1)
    hide_all_combo_list(self,1)
    if self.sender().objectName()=='Ok_pushButton' and geol_name=='GeolButton' and self.GeolButton.isEnabled()==True:
    # This condition select Qgis option to load data from QGIS layer panel for Geology layer
        self.PlaceHolderQlineEdit.hide()                          
        comboHeader = ['Formation*', 'Group','Supergroup', 'Description', 'Fm code', 'Rocktype 1','Rocktype 2','Polygon ID','Min Age','Max Age']
        self.combo_column_appender(self.colNames,geol_name)        
        qline_and_label_mover(340,200,340,220," Sill Text:",self.Sill_Label,self.Sill_LineEditor)
        qline_and_label_mover(340,280,340,300," Intrusion Text:",self.Intrusion_Label,self.Intrusion_LineEditor)
        qlineeditor_default_string(self,'sill','intrusive') 
        self.geolcheck = self.Geology_checkBox.checkState()

    elif self.sender().objectName()=='Ok_pushButton' and geol_name=='FaultButton' and self.FaultButton.isEnabled()==True:  
        # This condition select Qgis option to load data from QGIS layer panel for Fault Polyline 
        comboHeader      = ['Default Dip', 'Dip Direction','Feature', 'Dip Direction type', 'Fdipest', 'Point ID','Dip Dir Convention']
        self.combo_column_appender(self.colNames,geol_name)                                      
        DipDirectiontype_colNames =['num','alpha']
        DipDirectionConv_colNames =['Strike','Dip Direction']                                 
        self.cmbDescriptionLayerIDName.clear(),self.cmbRocktype2LayerIDName.clear()                                     
        self.cmbDescriptionLayerIDName.addItems(DipDirectiontype_colNames) 
        self.cmbRocktype2LayerIDName.addItems(DipDirectionConv_colNames)
        qline_and_label_mover(340,125,340,145," Fault Text:",self.Sill_Label,self.Sill_LineEditor)
        qline_and_label_mover(340,185,340,205," fdipest Text:",self.Intrusion_Label,self.Intrusion_LineEditor)
        qlineeditor_default_string(self,'Fault','shallow,steep,vertical')                  
        clear_partially_combo_list(self,7,1), clear_partially_combo_list(self,7,0)
        self.faultcheck= self.Fault_checkBox.checkState()

    elif self.sender().objectName()=='Ok_pushButton' and geol_name=='StructButton' and self.StructButton.isEnabled()==True:  
         # This condition select Qgis option to load data from QGIS layer panel for Structure Point
        comboHeader     = ['Dip*', 'Dip Direction*','Feature', 'Dip Dir Convention*', 'Overturned Field', 'Point ID']
        self.combo_column_appender(self.colNames,geol_name)
        DipDirectionConv_colNames =['Strike','Dip Direction']                      
        self.cmbDescriptionLayerIDName.clear()                                     
        self.cmbDescriptionLayerIDName.addItems(DipDirectionConv_colNames)                                    
        qline_and_label_mover(340,125,340,145," Bedding Text:",self.Sill_Label,self.Sill_LineEditor)
        qline_and_label_mover(340,185,340,205," Overturned Text:",self.Intrusion_Label,self.Intrusion_LineEditor)
        qlineeditor_default_string(self,'Bed','overturned')
        clear_partially_combo_list(self,6,1),clear_partially_combo_list(self,6,0)           
        self.structcheck= self.Structure_checkBox.checkState()

    else:
        pass
    label_mover(self,comboHeader)
    self.params_function_activator(True)                   
    self.geolcheck = self.Geology_checkBox.checkState()
    qgis_load_table(self,lyr,self.colNames) 
    self.Ok_pushButton.clicked.disconnect()        
    switch_qpush_in_qgis_option(self,geol_name)
    self.data_updater()
    self.dtm_push_activator()
    #print('finish with '+str(geol_name)+' button')
    return



def three_push_activator(self,flag):
    '''
    This function deal with Geol, Faul, Struct Qpushbutton.
    # flag =1, Geol-->True and Fault-->False and Struct-->False. flag=10 to Fault-->True and Struct-->True
    # flag =2, Fault-->True and Geol-->False and Struct-->False. flag=20 to Geol-->True and Struct-->True
    # flag =3, Geol-->True and Fault-->False and Struct-->False. flag=30 to Fault-->True and Geol-->True
    '''
    list_of_push_features  =[self.GeolButton, self.FaultButton, self.StructButton]
    for idx, elt in enumerate(list_of_push_features):
        if idx==0: 
            if flag==1:
                elt.setEnabled(True)
                list_of_push_features[idx+1].setEnabled(False)
                list_of_push_features[idx+2].setEnabled(False)
            elif flag==10:
                elt.setEnabled(False)
                list_of_push_features[idx+1].setEnabled(True)
                list_of_push_features[idx+2].setEnabled(True)
            else:
                pass
            break
        
        elif idx==1:
            if flag==2:
                elt.setEnabled(True)
                list_of_push_features[idx-1].setEnabled(False)
                list_of_push_features[idx+1].setEnabled(False) 
            elif flag==20:
                list_of_push_features[idx-1].setEnabled(True)
                list_of_push_features[idx+1].setEnabled(True)
            else:
                pass
            break
        elif idx==2:
            if flag==3:
                elt.setEnabled(True)
                list_of_push_features[idx-1].setEnabled(False)
                list_of_push_features[idx-2].setEnabled(False)
            elif flag==30:
                list_of_push_features[idx-1].setEnabled(True)
                list_of_push_features[idx-2].setEnabled(True) 
            else:
                pass
            break
        else:
            pass
    return          




def switch_qpush_in_qgis_option(self, name):
    '''
    This function is used to activate qpush button when Qgis option is chosen.
    ''' 
    try:
        if name=='StructButton':

            self.StructButton.setEnabled(False)
            if self.Fault_checkBox.isChecked()== True and self.Geology_checkBox.isChecked()== True:
                self.GeolButton.setEnabled(False),self.FaultButton.setEnabled(False)
                pass
            else:
                self.GeolButton.setEnabled(True), self.FaultButton.setEnabled(True)

            if self.Fault_checkBox.isChecked()== True:
                self.FaultButton.setEnabled(False)
            else:
                self.FaultButton.setEnabled(True)

            if self.Geology_checkBox.isChecked()== True:
                self.GeolButton.setEnabled(False)
            else:
                self.GeolButton.setEnabled(True) 

        elif name=='FaultButton':

            self.FaultButton.setEnabled(False)
            if self.Geology_checkBox.isChecked()== True and self.Structure_checkBox.isChecked()== True:
                self.GeolButton.setEnabled(False),self.StructButton.setEnabled(False)
            else:
                self.GeolButton.setEnabled(True), self.StructButton.setEnabled(True)
            if self.Structure_checkBox.isChecked()== True:
                self.StructButton.setEnabled(False)
            else:
                self.StructButton.setEnabled(True)

            if self.Geology_checkBox.isChecked()== True:
                self.GeolButton.setEnabled(False)
            else:
                self.GeolButton.setEnabled(True)

        elif name=='GeolButton': 
   
            self.GeolButton.setEnabled(False)
            if self.Fault_checkBox.isChecked()== True and self.Structure_checkBox.isChecked()== True:
                self.StructButton.setEnabled(False),self.FaultButton.setEnabled(False)
            else:
                self.StructButton.setEnabled(True),self.FaultButton.setEnabled(True)
            if self.Structure_checkBox.isChecked()== True:
                self.StructButton.setEnabled(False)
            else:
                self.StructButton.setEnabled(True)
            if self.Fault_checkBox.isChecked()== True:
                self.FaultButton.setEnabled(False)
            else:
                self.FaultButton.setEnabled(True) 

    except:
        pass

    return


