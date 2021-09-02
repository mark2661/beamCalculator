from PyQt5 import QtCore, QtGui, QtWidgets, uic

from beamCalculator.Ui.Show_dialog_error_messgae_box import showDialogErrorMessageBox

def isValidLoadLocation(location):
    #need tocheck if location is within length of beam
    return float(location) > 0

def isValidLoadMagnitude(magnitude):
    return float(magnitude) >= 0


class Add_pointLoad_dialog_window(QtWidgets.QDialog):
    def __init__(self):
        super(Add_pointLoad_dialog_window, self).__init__()
        uic.loadUi("/home/mark/Desktop/Beam Calculator/beamCalculator/Ui/UiFiles/Add_pointLoad_dialog_window.ui", self)
        self.Ok_button.clicked.connect(self.get_dialog_data)
        self.Cancel_button.clicked.connect(self.close)
        self.inputted_load_direction = self.inputted_load_magnitude = self.inputted_load_location = None

    def get_dialog_data(self):
        self.inputted_load_direction = 1 if self.loadDirectionComboBox.currentText() == "Up" else -1
        try:
            magnitude, location = self.loadMagnitudeInputField.text(), self.loadLocationInputField.text()
            if isValidLoadMagnitude(magnitude) and isValidLoadLocation(location):
                self.inputted_load_location = float(location)
                self.inputted_load_magnitude = float(magnitude) * self.inputted_load_direction
                self.close()
        except ValueError:
            showDialogErrorMessageBox()
            self.loadLocationInputField.clear()
            self.loadMagnitudeInputField.clear()


