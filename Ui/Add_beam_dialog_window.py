# -*- coding: utf-8 -*-

# Form implementation generated from reading UiFiles file 'UiFiles/Add_beam_dialog_window.UiFiles'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, uic


class Add_beam_dialog_window(QtWidgets.QDialog):
    def __init__(self):
        super(Add_beam_dialog_window, self).__init__()
        uic.loadUi("/home/mark/Desktop/Beam Calculator/beamCalculator/Ui/UiFiles/Add_beam_dialog_window.ui", self)
        self.buttonBox.accepted.connect(self.get_dialog_data)
        self.inputted_beam_length = None

    def get_dialog_data(self):
        self.inputted_beam_length = self.BeamLengthInputField.text()

