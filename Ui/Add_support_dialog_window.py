from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from beamCalculator.Ui.Show_dialog_error_messgae_box import showDialogErrorMessageBox

def isValidInputLocation(length):
    return float(length) > 0

class Add_support_dialog_window(QtWidgets.QDialog):
    def __init__(self):
        super(Add_support_dialog_window, self).__init__()
        uic.loadUi("/home/mark/Desktop/Beam Calculator/beamCalculator/Ui/UiFiles/Add_support_dialog_window.ui", self)
        self.Ok_button.clicked.connect(self.get_dialog_data)
        self.Cancel_button.clicked.connect(self.close)
        self.support_type = self.support_location = None

    def get_dialog_data(self):
        try:
            self.support_type = self.supportTypeComboBox.currentText().split()[0].lower()
            if isValidInputLocation(self.supportLocationInputField.text()):
                self.support_location = float(self.supportLocationInputField.text())
                self.close()
        except ValueError:
            showDialogErrorMessageBox()
            self.supportLocationInputField.clear()





