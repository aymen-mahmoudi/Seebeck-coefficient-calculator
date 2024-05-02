#!/usr/bin/env python

##############################################################################
##
# This file is part of the Seebeck coefficient calculator project
##
# SHG data fitting is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
##
##############################################################################

__author__ = ["Aymen Mahmoudi"]
__license__ = "GPL"
__date__ = "01/02/2023"

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5 import QtGui, QtCore
 

import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from functions import*

#  import the  / picture ressource :

#ui, _ = loadUiType('gui.ui')      # from gui.ui
from gui import Ui_Form  as ui    # from gui.py

import picture_ressource



class MainWindow(QWidget, ui):

    def __init__(self):
        QWidget.__init__(self)
        #self.setWindowIcon(QtGui.QIcon('logo.jpg')) choose logo from the designer
        self.setupUi(self)
        # desactivate buttons
        #self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        #self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        # function to setup buttons
        self.HandleButtons()
        
        
    def HandleButtons(self):
        self.clickHere_pushButton.clicked.connect(self.essential_values)
        # output (set)
        self.clickHere_pushButton.clicked.connect(self.set_seebeck)    
        
        

       

                

    
    def essential_values(self):
        # Global Varilables

        print ('essential values here')
        self.T = 0 ; self.n = 0 ;  self.m = 0
        

        


        self.T = float(self.get_T())
        self.m = float(self.get_m())
        self.n = float(self.get_n())

        
        
     

       
        

    def get_T(self):
        T = self.T_lineEdit.text()
        return T


    def get_m(self):
        E = self.m_lineEdit.text()
        return E
    
    def get_n(self):
        n = self.n_lineEdit.text()
        return n

    
  

    #function showing value

    def set_seebeck(self):
        self.seebeck_output_label.setText(str(np.round(seebeck(self.T,self.m,self.n),4)))


    


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # hold ui
    app.exec_()

if __name__ == "__main__" :
    main()



