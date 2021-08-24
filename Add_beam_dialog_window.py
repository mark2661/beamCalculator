# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Add_beam_dialog_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, uic


# class Ui_Dialog(object):
#     def setupUi(self, Dialog):
#         Dialog.setObjectName("Dialog")
#         Dialog.resize(731, 74)
#         self.formLayout = QtWidgets.QFormLayout(Dialog)
#         self.formLayout.setObjectName("formLayout")
#         self.label_2 = QtWidgets.QLabel(Dialog)
#         self.label_2.setObjectName("label_2")
#         self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
#         self.BeamLengthInputField = QtWidgets.QLineEdit(Dialog)
#         self.BeamLengthInputField.setObjectName("BeamLengthInputField")
#         self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.BeamLengthInputField)
#         self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
#         self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
#         self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
#         self.buttonBox.setObjectName("buttonBox")
#         self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)
#
#         self.retranslateUi(Dialog)
#         self.buttonBox.accepted.connect(Dialog.accept)
#         self.buttonBox.rejected.connect(Dialog.reject)
#         QtCore.QMetaObject.connectSlotsByName(Dialog)
#
#     def retranslateUi(self, Dialog):
#         _translate = QtCore.QCoreApplication.translate
#         Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
#         self.label_2.setText(_translate("Dialog", "Beam Length:"))
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

class Add_beam_dialog_window(QtWidgets.QDialog):
    def __init__(self):
        super(Add_beam_dialog_window, self).__init__()
        uic.loadUi("ui/Add_beam_dialog_window.ui", self)
