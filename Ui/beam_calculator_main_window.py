# -*- coding: utf-8 -*-

# Form implementation generated from reading .uiFiles file '.uiFiles/beam_calculator_main_window..uiFiles'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Add_beam_dialog_window import Ui_Dialog as Ui_add_beam_dialog
from Add_support_dialog_window import Ui_Dialog as Ui_add_support_dialog
from Add_pointLoad_dialog_window import Ui_Dialog as Ui_add_pointLoad_dialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 550)
        MainWindow.setMinimumSize(QtCore.QSize(860, 550))
        MainWindow.setMaximumSize(QtCore.QSize(860, 570))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        """
        *********************************************************************
        Code for ADDBeamButton
        """
        self.AddBeamButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddBeamButton.setMinimumSize(QtCore.QSize(120, 0))
        self.AddBeamButton.setObjectName("AddBeamButton")
        #self.AddBeamButton.clicked.connect(self.open_add_beam_window)
        """
        ********************************************************************
        """
        self.verticalLayout.addWidget(self.AddBeamButton)
        spacerItem = QtWidgets.QSpacerItem(120, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        """
        *********************************************************************
        Code for ADDSupportButton
        """
        self.AddSupportButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddSupportButton.setMinimumSize(QtCore.QSize(120, 0))
        self.AddSupportButton.setObjectName("AddSupportButton")
        #self.AddSupportButton.clicked.connect(self.open_add_support_window)
        """
        ********************************************************************
        """
        self.verticalLayout.addWidget(self.AddSupportButton)
        spacerItem1 = QtWidgets.QSpacerItem(120, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        """
        *********************************************************************
        Code for ADDPointLoadButton
        """
        self.AddPointLoadButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddPointLoadButton.setMinimumSize(QtCore.QSize(120, 0))
        self.AddPointLoadButton.setObjectName("AddPointLoadButton")
        #self.AddPointLoadButton.clicked.connect(self.open_add_pointLoad_window)
        """
        ********************************************************************
        """
        self.verticalLayout.addWidget(self.AddPointLoadButton)
        spacerItem2 = QtWidgets.QSpacerItem(120, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.AddMomentButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddMomentButton.setMinimumSize(QtCore.QSize(120, 0))
        self.AddMomentButton.setObjectName("AddMomentButton")
        self.verticalLayout.addWidget(self.AddMomentButton)
        spacerItem3 = QtWidgets.QSpacerItem(120, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.AddUDLButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddUDLButton.setMinimumSize(QtCore.QSize(120, 0))
        self.AddUDLButton.setObjectName("AddUDLButton")
        self.verticalLayout.addWidget(self.AddUDLButton)
        spacerItem4 = QtWidgets.QSpacerItem(120, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(120, 0))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.ForceUnitComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.ForceUnitComboBox.setMinimumSize(QtCore.QSize(120, 0))
        self.ForceUnitComboBox.setObjectName("ForceUnitComboBox")
        self.ForceUnitComboBox.addItem("")
        self.ForceUnitComboBox.addItem("")
        self.verticalLayout.addWidget(self.ForceUnitComboBox)
        spacerItem5 = QtWidgets.QSpacerItem(120, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(120, 0))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.LengthUnitComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.LengthUnitComboBox.setMinimumSize(QtCore.QSize(120, 0))
        self.LengthUnitComboBox.setObjectName("LengthUnitComboBox")
        self.LengthUnitComboBox.addItem("")
        self.LengthUnitComboBox.addItem("")
        self.LengthUnitComboBox.addItem("")
        self.verticalLayout.addWidget(self.LengthUnitComboBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.GraphicsViewWindow = QtWidgets.QGraphicsView(self.centralwidget)
        self.GraphicsViewWindow.setObjectName("GraphicsViewWindow")
        self.horizontalLayout.addWidget(self.GraphicsViewWindow)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(308, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.SolveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SolveButton.setMinimumSize(QtCore.QSize(200, 40))
        self.SolveButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.SolveButton.setObjectName("SolveButton")
        self.horizontalLayout_2.addWidget(self.SolveButton)
        self.ResetButton = QtWidgets.QPushButton(self.centralwidget)
        self.ResetButton.setMinimumSize(QtCore.QSize(200, 40))
        self.ResetButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.ResetButton.setObjectName("ResetButton")
        self.horizontalLayout_2.addWidget(self.ResetButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def open_add_beam_window(self): #Group into one open_dialog_window function with a dialog..uiFiles parameter
    #     dialog = QtWidgets.QDialog()
    #     dialog..uiFiles = Ui_add_beam_dialog()
    #     dialog..uiFiles.setupUi(dialog)
    #     dialog.exec_()
    #     dialog.show()
    #
    # def open_add_support_window(self):
    #     dialog = QtWidgets.QDialog()
    #     dialog..uiFiles = Ui_add_support_dialog()
    #     dialog..uiFiles.setupUi(dialog)
    #     dialog.exec_()
    #     dialog.show()
    #
    # def open_add_pointLoad_window(self):
    #     dialog = QtWidgets.QDialog()
    #     dialog..uiFiles = Ui_add_pointLoad_dialog()
    #     dialog..uiFiles.setupUi(dialog)
    #     dialog.exec_()
    #     dialog.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AddBeamButton.setText(_translate("MainWindow", "Add Beam"))
        self.AddSupportButton.setText(_translate("MainWindow", "Add Support"))
        self.AddPointLoadButton.setText(_translate("MainWindow", "Add point load"))
        self.AddMomentButton.setText(_translate("MainWindow", "Add Moment"))
        self.AddUDLButton.setText(_translate("MainWindow", "Add UDL"))
        self.label.setText(_translate("MainWindow", "Foce Unit"))
        self.ForceUnitComboBox.setItemText(0, _translate("MainWindow", "N"))
        self.ForceUnitComboBox.setItemText(1, _translate("MainWindow", "kN"))
        self.label_2.setText(_translate("MainWindow", "Length Unit"))
        self.LengthUnitComboBox.setItemText(0, _translate("MainWindow", "m"))
        self.LengthUnitComboBox.setItemText(1, _translate("MainWindow", "cm"))
        self.LengthUnitComboBox.setItemText(2, _translate("MainWindow", "mm"))
        self.SolveButton.setText(_translate("MainWindow", "Solve"))
        self.ResetButton.setText(_translate("MainWindow", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
