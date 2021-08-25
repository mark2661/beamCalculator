from PyQt5 import QtWidgets, uic

from Calculator.CrossSection.RectangularCrossSection import RectangularCrossSection


class Rectangular_cross_section_dialog_window(QtWidgets.QDialog):
    def __init__(self):
        super(Rectangular_cross_section_dialog_window, self).__init__()
        uic.loadUi("/home/mark/Desktop/Beam Calculator/beamCalculator/Ui/uiFiles/Rectangular_cross_section_dialog_window.ui", self)
        self.buttonBox.accepted.connect(self.get_dialog_data)
        self.cross_section_length = self.cross_section_width = None
        self.user_cross_section = None

    def get_dialog_data(self):
        self.cross_section_width = int(self.CrossSectionWidthInputField.text())
        self.cross_section_length = int(self.CrossSectionLengthInputField.text())
        self.user_cross_section = RectangularCrossSection(self.cross_section_width, self.cross_section_length)

    def get_user_cross_section(self):
        return self.user_cross_section
