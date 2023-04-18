'''
This python module import the following features
: QCombobox feature and it's associated label name
: QlineEditor feature and its associated label name
'''

from PyQt5.QtGui import QFont,QPixmap

#from qgis.utils import iface
from qgis.core import QgsProject
from PyQt5 import QtGui,QtCore
import os
#from .help_function import save_config_msg
from .clear_features import hide_all_combo_list, clear_all_label
#from .help_function import welcome_msg



def update_file_path(filename,list_of_roi_names):
        '''
        This function is used to update the layer path name once ROI is used
        The name of the layer will be replaced by the clipped name
        '''
        oldname            = [a for a in filename.split('\\')][-1]
        ext                = oldname.split('.')[-1]
        newname            = [b for b in list_of_roi_names if oldname.split('.')[0] in b][0]+'.'+str(ext)
        # print('oldname {} '.format(oldname))
        # print('newname {} '.format(newname))
        maxreplace = 1
        result = newname.join(filename.rsplit(oldname, maxreplace))
        return result



def dynamic_qeditor(label,X1,Y1):
    '''
    This function create dynamic QLineEditor which is then move into X1,Y1 position.
    '''
    label.move(X1,Y1)
    return 


def dynamic_label(Sill_Msg,label,X1,Y1): 
    '''
    This function create dynamic QLabel which is then move into X1,Y1 position.
    :Sill_Msg: Label name that could explain the meaning of the value to enter into the QlineEditor.
    :label: qt label name, i.e .self.sill_label.
    :X1,Y1 is the (x,y) coordinate of the label feature into Qt MainWindow.
    '''                            
    label.setText(Sill_Msg)                     
    label.setFont(QFont("Sanserif",10))
    label.move(X1,Y1)


def label_mover(self,geol_comboHeader):
        '''
        This function create dynamic label which is then move into X1,Y1*idx position.
        : The label break is to constraint empty label into Qt framework.
        '''
        self.label_list       = [self.moving_Label_1,self.moving_Label_2,self.moving_Label_3,self.moving_Label_4,self.moving_Label_5,self.moving_Label_6,self.moving_Label_7,self.moving_Label_8,self.moving_Label_9,self.moving_Label_10]
        for idx, combo_elt in enumerate(geol_comboHeader):
            self.label_list[idx].setText(geol_comboHeader[idx])                     
            self.label_list[idx].setFont(QFont("Sanserif",10))
            if idx==len(geol_comboHeader)-1:
                break


def qline_and_label_mover(X1,Y1,X2,Y2,msg1,label1,label2):
        '''
        This function is a purpose built to move both Qlabel and QLineEditor.
        '''
        dynamic_label(msg1,label1,X1,Y1)
        dynamic_qeditor(label2,X2,Y2)


def qlineeditor_default_string(self,string1, string2):
    '''
    This function enter default string value into QLineEditor. 
    '''
    self.Sill_LineEditor.setText(str(string1))
    self.Intrusion_LineEditor.setText(str(string2))
    

def welcoming_image(self,flag):
    '''
    This function is used to show the welcome image for flag variable equal to 1.
    This code sets an image file as the background of a label widget in a PyQt5 application.  
    It starts by defining the base directory and the image file path, and then sets the image as the background of the label. 
    The image is then scaled to fit the label while keeping its aspect ratio and is set as the pixmap of the label. 
    The scaled contents are set to false to meet image ratio versus label ratio.
    '''
    if flag==1:
        BASE_DIR     = os.path.dirname(__file__)
        Image_path   = str(BASE_DIR)+'/ImageMapToLoop.png'
        self.ImageLabel.setStyleSheet("background-image : url("+str(Image_path)+");border : 0.5px solid blue")
        self.pixmap  = QPixmap(str(Image_path)).scaled(self.ImageLabel.size(),QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation)
        self.ImageLabel.setPixmap(self.pixmap)
        self.ImageLabel.setScaledContents(False)
    else:
        self.ImageLabel.hide()


def save_activator(self,flag):
    '''
    This function is used to activate the save button)
    '''
    if flag==0:
        self.Map2Loop_Button.setEnabled(False) 
        self.Saveconfig_pushButton.setEnabled(False) 
        self.LoopStructural_Button.setEnabled(False) 
    elif flag==1:
       self.Map2Loop_Button.setVisible(True)
       self.Saveconfig_pushButton.setVisible(True)
       self.LoopStructural_Button.setVisible(True)
    else:
        pass


def icon_indexer(self):
    '''
    This function is used to append the icon to the QPushButton
    '''
    BASE_DIR       = os.path.dirname(__file__)
    Image_path     = str(BASE_DIR)+'/Icon/'
    list_of_images = ['project.png','geol.png','fault.png','struct.png','orient.png','dtm.png','roi.png','dh.png','section.png','fold.png','config.png' ]
    items          = [self.PrjImage,self.GeolButton,self.FaultButton,self.StructButton,self.OrientationButton,self.DTMButton,self.ROIButton,self.DrillholesButton,self.SectionsButton,self.FoldButton,self.ConfigButton]
    for idx, label in enumerate(items):
        if idx==0:
           label.setPixmap(QPixmap(str(Image_path)+str(list_of_images[idx])))
           label.setScaledContents(True)
        else:
           label.setIcon(QtGui.QIcon(str(Image_path)+str(list_of_images[idx])))
        label.setStyleSheet("QPushButton { text-align: left; }")
        #label.setLayoutDirection(QtCore.Qt.RightToLeft) #RightToLeft #LeftToRight
        #self.GeolButton.setIcon(QtGui.QIcon(str(Image_path)+'geol.png'))
 
 
def list_all_layers(self):
    '''
    This function return the list of layers availaible in qgis-layer panel
    '''
    layers_list = QgsProject.instance().mapLayers().values()
    names       = [layer.name() for layer in layers_list]
    paths       = [name.dataProvider().dataSourceUri() for name in layers_list]
    self.layer_dict = dict(zip(names,paths))
    self.objec_dict = dict(zip(names,layers_list))
    if self.sender().objectName()=='Qgis_checkBox'and self.GeolButton.isEnabled()==True and self.sender_name=='GeolButton':
        names = [a.name() for a in layers_list if type(a).__name__=='QgsVectorLayer' and a.wkbType()==6]
    elif self.sender().objectName()=='Qgis_checkBox'and self.FaultButton.isEnabled()==True and self.sender_name=='FaultButton':
        names = [a.name() for a in layers_list if type(a).__name__=='QgsVectorLayer' and a.wkbType()==5]
    elif self.sender().objectName()=='Qgis_checkBox'and self.StructButton.isEnabled()==True and self.sender_name=='StructButton':
        names = [a.name() for a in layers_list if type(a).__name__=='QgsVectorLayer' and a.wkbType()==1]
    elif self.sender().objectName()=='Qgis_checkBox'and self.DTMButton.isEnabled()==True:# and self.sender_name=='StructButton':
        names = [a.name() for a in layers_list if type(a).__name__=='QgsRasterLayer']   
    else:
        pass
    self.Qgis_comboBox.addItems(names) 
    return self.layer_dict,self.objec_dict 


def activate_config_file(self):
    '''
    This function activate the Save Config File Qpushbutton only when the dtm,geol,struct,and fault parameters are all saved.
    '''   
    
    try:
        if self.Geology_checkBox.isChecked()==True and self.Fault_checkBox.isChecked()==True and self.Structure_checkBox.isChecked()==True and self.DTM_checkBox.isChecked()==True and self.folder_name=='FolderSearch_Button':
            self.Saveconfig_pushButton.setEnabled(True)  
        else:
            self.Saveconfig_pushButton.setEnabled(False)
    except:
        pass
    return


def activate_loader_checkbox(self, flag):
    '''
    This function activate and desactivate(greyed it or disabled it) the Load layer tick box all saved.
    # flag =0: to setEnabled to False
    # flag =1: to setEnabled to True
    '''   
    try:
        L=[self.Geology_checkBox,self.Fault_checkBox,self.Structure_checkBox,self.DTM_checkBox]
        if flag==0:
            for i in range(len(L)):
                L[i].setEnabled(False)
        else:
            for i in range(len(L)):
                L[i].setEnabled(True)
    except:
    
        pass
    return


def reset_all_features(self):
    '''
    This method resets all the features.
    The code define a method called "reset_all_features" for an object (presumably a GUI element) in Python. 
    The method uncheck four checkboxes Geology_checkBox, Fault_checkBox, Structure_checkBox, DTM_checkBox 
    and enable it associated pushbutton FaultButton, GeolButton, StructButton, DTMButton, respectively. 
    '''
    # Loader Checkbox options 
    self.Qgis_checkBox.setChecked(False)
    self.Aus_checkBox.setChecked(False)
    self.File_checkBox.setChecked(False)
    self.Http_checkBox.setChecked(False)
    
    self.Qgis_comboBox.clear()
    self.Qgis_comboBox.setVisible(False)
    self.Ok_pushButton.setVisible(False)
    # Main option
    # self.FaultButton.setEnabled(True)
    # self.GeolButton.setEnabled(True)
    # self.StructButton.setEnabled(True)
    # self.DTMButton.setEnabled(True)
    # Main option checkbox
    self.Geology_checkBox.setChecked(False)
    self.Fault_checkBox.setChecked(False)
    self.Structure_checkBox.setChecked(False)
    self.DTM_checkBox.setChecked(False)
   
    try:
        if self.reset_flag=='File_checkBox':
           self.ImageLabel.setVisible(True)
           welcoming_image(self,1)
           self.close()
    except:
        pass
    return


def set_to_tristate(label):
    '''
    This function set to tristate any checkbox
    '''
    if label.isCheckable():
        label.setTristate(True)

    return


def reset_after_run(self):
    '''
    This function reset the all pyqt features 
    '''
    hide_all_combo_list(self,0)
    self.CRS_LineEditor.setVisible(False)                     
    self.CRS_label.setVisible(False)
    self.SearchFolder.clear()
    # reset all checkbox and reactivate all pushbutton
    self.GeolButton.setEnabled(True)
    self.FaultButton.setEnabled(True)
    self.StructButton.setEnabled(True)
    self.DTMButton.setEnabled(True)
    # reset all checkbox pushbutton
    reset_all_features(self)
    # reset all checkbox 
    clear_all_label(self)


def qpush_desactivator(self,flag):
    '''
    This function enable qpush based on some permutations.
    '''
   
    try:
        list  =[self.GeolButton,self.FaultButton,self.StructButton]
        clist = [self.Geology_checkBox,self.Fault_checkBox,self.Structure_checkBox]
        if flag=='GeolButton':
                try:
                    if len(self.a)==2:
                        list= self.a
                        clist=self.b
                    if len(self.a)==1:
                      self.DTMButton.setEnabled(True)  
                except:
                    pass
                self.a=list
                self.b=clist
                for val,cval in zip(self.a,self.b):
                    if cval.isChecked()== True:
                        val.setEnabled(False)
                    else: 
                        val.setEnabled(True)
                self.GeolButton.setEnabled(False)
                
                if self.Fault_checkBox.isChecked()== True:
                   self.FaultButton.setEnabled(False)
                if self.Struct_checkBox.isChecked()== True:
                   self.StructButton.setEnabled(False)
                return self.a, self.b
        
        elif flag=='FaultButton':
                try:
                    if len(self.a)==2:
                        list= self.a
                        clist=self.b
                    if len(self.a)==1:
                       self.DTMButton.setEnabled(True)  
                except:
                    pass
                self.a=list
                self.b=clist
                for val,cval in zip(self.a,self.b):
                    if cval.isChecked()== True:
                        val.setEnabled(False) 
                    else:
                        val.setEnabled(True)
                self.FaultButton.setEnabled(False)
                if self.Struct_checkBox.isChecked()== True:
                   self.StructButton.setEnabled(False)
                if self.Geology_checkBox.isChecked()== True:
                   self.GeolButton.setEnabled(False)   
                return self.a, self.b
        
        elif flag=='StructButton':
                try:
                    if len(self.a)==2:
                        list= self.a
                        clist=self.b
                    if len(self.a)==1:
                      self.DTMButton.setEnabled(True)  
                except:
                    pass
                self.a=list
                self.b=clist
                for val,cval in zip(self.a,self.b):
                    if cval.isChecked()== True:
                        val.setEnabled(False) 
                    else:
                        val.setEnabled(True) 
                self.StructButton.setEnabled(False)
                if self.Fault_checkBox.isChecked()== True:
                   self.FaultButton.setEnabled(False)
                if self.Geology_checkBox.isChecked()== True:
                   self.GeolButton.setEnabled(False)
                return self.a, self.b
    except:
        pass
    #print('passed the fault stage')
    return
