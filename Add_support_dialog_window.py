# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Add_support_dialog_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, uic

class Add_support_dialog_window(QtWidgets.QDialog):
    def __init__(self):
        super(Add_support_dialog_window, self).__init__()
        uic.loadUi("ui/Add_support_dialog_window.ui", self)
        self.buttonBox.accepted.connect(self.get_dialog_data)
        self.supports = []
        self.support_type = self.support_location = None

    def get_dialog_data(self):
        self.support_type = self.supportTypeComboBox.currentText()
        self.support_location = self.SupportLocationInputField.text()
        self.supports.append((self.support_type, self.support_location))


