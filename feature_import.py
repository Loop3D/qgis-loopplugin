'''
This python module import the following features
: QCombobox feature and it's associated label name
: QlineEditor feature and its associated label name
'''
from PyQt5.QtGui import QFont


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
