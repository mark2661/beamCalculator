# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Add_support_dialog_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(599, 133)
        Dialog.setMinimumSize(QtCore.QSize(599, 133))
        Dialog.setMaximumSize(QtCore.QSize(599, 133))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.TogglePinSupportButton = QtWidgets.QPushButton(Dialog)
        self.TogglePinSupportButton.setCheckable(False)
        self.TogglePinSupportButton.setObjectName("TogglePinSupportButton")
        self.verticalLayout.addWidget(self.TogglePinSupportButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ToggleRollerSupportButton = QtWidgets.QPushButton(Dialog)
        self.ToggleRollerSupportButton.setObjectName("ToggleRollerSupportButton")
        self.verticalLayout_2.addWidget(self.ToggleRollerSupportButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ToggleFixedSupportButton = QtWidgets.QPushButton(Dialog)
        self.ToggleFixedSupportButton.setObjectName("ToggleFixedSupportButton")
        self.verticalLayout_3.addWidget(self.ToggleFixedSupportButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.SupportLocationInputField = QtWidgets.QLineEdit(Dialog)
        self.SupportLocationInputField.setObjectName("SupportLocationInputField")
        self.horizontalLayout.addWidget(self.SupportLocationInputField)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.TogglePinSupportButton.setText(_translate("Dialog", "Pin Support"))
        self.ToggleRollerSupportButton.setText(_translate("Dialog", "Roller Support"))
        self.ToggleFixedSupportButton.setText(_translate("Dialog", "Fixed Support"))
        self.label.setText(_translate("Dialog", "Support Location: "))

    def accept(self):
        pass
    def reject(self):
        pass
