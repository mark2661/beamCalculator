from PyQt5 import QtWidgets, uic

from Calculator.CrossSection.SquareCrossSection import SquareCrossSection


class Square_cross_section_dialog_window(QtWidgets.QDialog):
    def __init__(self):
        super(Square_cross_section_dialog_window, self).__init__()
        uic.loadUi("/home/mark/Desktop/Beam Calculator/beamCalculator/Ui/uiFiles/Square_cross_section_dialog_window.ui", self)
        self.buttonBox.accepted.connect(self.get_dialog_data)
        self.cross_section_length = None
        self.user_cross_section = None

    def get_dialog_data(self):
        self.cross_section_length = int(self.CrossSectionLengthInputField.text())
        self.user_cross_section = SquareCrossSection(self.cross_section_length)

    def get_user_cross_section(self):
        return self.user_cross_section
