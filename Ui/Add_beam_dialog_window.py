# -*- coding: utf-8 -*-

# Form implementation generated from reading UiFiles file 'UiFiles/Add_beam_dialog_window.UiFiles'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *

class InputError(Exception):
    print("input error")

class Add_beam_dialog_window(QtWidgets.QDialog):
    def __init__(self):
        super(Add_beam_dialog_window, self).__init__()
        uic.loadUi("/home/mark/Desktop/Beam Calculator/beamCalculator/Ui/UiFiles/Add_beam_dialog_window.ui", self)
        self.Ok_button.clicked.connect(self.get_dialog_data)
        self.Cancel_button.clicked.connect(self.close)
        self.inputted_beam_length = None

    def get_dialog_data(self):
        try:
            length = self.BeamLengthInputField.text()
            self.inputted_beam_length = float(length)
            self.close()
        except ValueError:
            self.showErrorMessageBox()


    def showErrorMessageBox(self):
        self.msg = QMessageBox()
        self.msg.setText("InvalidInput")
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()



