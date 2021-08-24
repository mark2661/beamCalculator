# -*- coding: utf-8 -*-

# Form implementation generated from reading .uiFiles file '.uiFiles/Add_pointLoad_dialog_window..uiFiles'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, uic

class Add_pointLoad_dialog_window(QtWidgets.QDialog):
    def __init__(self):
        super(Add_pointLoad_dialog_window, self).__init__()
        uic.loadUi(".uiFiles/Add_pointLoad_dialog_window..uiFiles",self)
        self.buttonBox.accepted.connect(self.get_dialog_data)
        self.loads = []
        self.inputted_load_direction = self.inputted_load_magnitude = self.inputted_load_location = None

    def get_dialog_data(self):
        self.inputted_load_magnitude = self.LoadMagnitudeInputField.text()
        self.inputted_load_location = self.LoadLocationInputField.text()
        self.inputted_load_direction = self.LoadDirectionComboBox.currentText()
        self.loads.append((self.inputted_load_direction, self.inputted_load_magnitude, self.inputted_load_location))

