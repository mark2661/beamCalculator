# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Add_pointLoad_dialog_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, uic


# class Ui_Dialog(object):
#     def setupUi(self, Dialog):
#         Dialog.setObjectName("Dialog")
#         Dialog.resize(364, 186)
#         self.formLayout = QtWidgets.QFormLayout(Dialog)
#         self.formLayout.setObjectName("formLayout")
#         self.label_4 = QtWidgets.QLabel(Dialog)
#         self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.label_4.setObjectName("label_4")
#         self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
#         self.comboBox = QtWidgets.QComboBox(Dialog)
#         self.comboBox.setObjectName("comboBox")
#         self.comboBox.addItem("")
#         self.comboBox.addItem("")
#         self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
#         self.label_2 = QtWidgets.QLabel(Dialog)
#         self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
#         self.label_2.setIndent(0)
#         self.label_2.setObjectName("label_2")
#         self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
#         self.LoadLocationInputField = QtWidgets.QLineEdit(Dialog)
#         self.LoadLocationInputField.setObjectName("LoadLocationInputField")
#         self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.LoadLocationInputField)
#         self.label = QtWidgets.QLabel(Dialog)
#         self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
#         self.label.setIndent(0)
#         self.label.setObjectName("label")
#         self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
#         self.LoadMagnitudeInputfield = QtWidgets.QLineEdit(Dialog)
#         self.LoadMagnitudeInputfield.setObjectName("LoadMagnitudeInputfield")
#         self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.LoadMagnitudeInputfield)
#         self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
#         self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
#         self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
#         self.buttonBox.setObjectName("buttonBox")
#         self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
#
#         self.retranslateUi(Dialog)
#         self.buttonBox.accepted.connect(Dialog.accept)
#         self.buttonBox.rejected.connect(Dialog.reject)
#         QtCore.QMetaObject.connectSlotsByName(Dialog)
#
#     def retranslateUi(self, Dialog):
#         _translate = QtCore.QCoreApplication.translate
#         Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
#         self.label_4.setText(_translate("Dialog", "Direction"))
#         self.comboBox.setItemText(0, _translate("Dialog", "Up"))
#         self.comboBox.setItemText(1, _translate("Dialog", "Down"))
#         self.label_2.setText(_translate("Dialog", "Load Magnitude"))
#         self.label.setText(_translate("Dialog", "Load Location"))
#
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())

class Add_pointLoad_dialog_window(QtWidgets.QDialog):
    def __init__(self):
        super(Add_pointLoad_dialog_window, self).__init__()
        uic.loadUi("ui/Add_pointLoad_dialog_window.ui",self)
        self.buttonBox.accepted.connect(self.get_dialog_data)
        self.loads = []
        self.inputted_load_direction = self.inputted_load_magnitude = self.inputted_load_location = None

    def get_dialog_data(self):
        self.inputted_load_magnitude = self.LoadMagnitudeInputField.text()
        self.inputted_load_location = self.LoadLocationInputField.text()
        self.inputted_load_direction = self.LoadDirectionComboBox.currentText()
        self.loads.append((self.inputted_load_direction, self.inputted_load_magnitude, self.inputted_load_location))

