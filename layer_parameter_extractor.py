'''
This python module generate data from individual layers
When the Load >< is activated, the resulting data are appended into Qt frame

'''
from .load_vectors import shape_file_loader,xlayer_reader,create_json_file
from .feature_import import label_mover,qline_and_label_mover,qlineeditor_default_string

######
def create_geology_idname(self):
    '''
    Once Load Geology is released, the function will return Geology IDs which are filled in combobox associated to the layer in Qt framework.
    '''
    self.PlaceHoldercomboBox.setVisible(True)
    self.PlaceHolderQlineEdit.hide()
    self.CRS_LineEditor.setVisible(True)                     
    self.CRS_label.setVisible(True)                          
    self.QPushbutton_functionActivator(False,self.FaultButton,self.StructButton,self.DTMButton)
    p,self.GeolPath  = self.activate_layers(self.sender().text())                                    
    if self.GeolButton.objectName()=='GeolButton':
        self.GeolPath= self.GeolPath
    geol_comboHeader = ['Formation*', 'Group*','Supergroup*', 'Description*', 'Fm code*', 'Rocktype 1*','Rocktype 2*','Polygon ID*','Min Age*','Max Age*']
    label_mover(self,geol_comboHeader)
    self.colNames    = xlayer_reader()
    self.combo_column_appender(self.colNames,self.GeolButton.objectName())        
    qline_and_label_mover(320,210,320,230," Sill Text:",self.Sill_Label,self.Sill_LineEditor)
    qline_and_label_mover(320,280,320,300," Intrusion Text:",self.Intrusion_Label,self.Intrusion_LineEditor)
    qlineeditor_default_string(self,'sill','intrusive')
    self.Help_TextEdit.setText(self.list_of_infos[0])  
    self.params_function_activator(True)                   
    self.geolcheck = self.Geology_checkBox.checkState()
    self.Save_pushButton.clicked.connect(self.save_geol_IdName)
    self.CRS_LineEditor.setText(str('28350'))     
    return
