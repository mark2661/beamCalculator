from PyQt5 import QtCore, QtGui, QtWidgets, uic

from beamCalculator.Ui.Show_dialog_error_messgae_box import showDialogErrorMessageBox

def isValidLoadMagnitude(magnitude):
    return float(magnitude) >= 0

def isValidStartLoadLocation(start, end):
    #need tocheck if location is within length of beam
    return float(start) > 0 and start <= end

def isValidLoadEndLocation(end, start):
    # need tocheck if location is within length of beam
    return float(end) >= 0 and end >= start

def isValidOrder(order):
    return int(order) >= 0

def isValidUDL(magnitude, start, end, order):
    return isValidLoadMagnitude(magnitude) and isValidStartLoadLocation(start, end) \
           and isValidLoadEndLocation(end, start) and isValidOrder(order)


class Add_UDL_dialog_window(QtWidgets.QDialog):
    def __init__(self):
        super(Add_UDL_dialog_window, self).__init__()
        uic.loadUi("/home/mark/Desktop/Beam Calculator/beamCalculator/Ui/UiFiles/Add_UDL_dialog_window.ui", self)
        self.Ok_button.clicked.connect(self.get_dialog_data)
        self.Cancel_button.clicked.connect(self.close)
        self.inputted_load_direction = self.inputted_load_magnitude = self.inputted_load_start_location = self.inputted_load_end_location = self.inputted_load_order = None

    def get_dialog_data(self):
        self.inputted_load_direction = 1 if self.loadDirectionComboBox.currentText() == "Up" else -1
        #self.inputted_load_direction = 1 if self.loadDirectionComboBox.currentText() == "Down" else -1
        try:
            magnitude = self.loadMagnitudeInputField.text()
            start_location = self.loadStartLocationInputField.text()
            end_location = self.loadEndLocationInputField.text()
            order = self.loadOrderInputField.text()
            if isValidUDL(magnitude, start_location, end_location, order):
                self.inputted_load_magnitude = float(magnitude) * self.inputted_load_direction
                self.inputted_load_start_location = float(start_location)
                self.inputted_load_end_location = float(end_location)
                self.inputted_load_order = int(order)
                self.close()
        except ValueError:
            self.loadMagnitudeInputField.clear()
            self.loadStartLocationInputField.clear()
            self.loadEndLocationInputField.clear()
            self.loadOrderInputField.clear()
            showDialogErrorMessageBox()


