from PyQt5 import QtWidgets, uic
from Add_beam_dialog_window import Add_beam_dialog_window
from Add_support_dialog_window import Add_support_dialog_window
from Add_pointLoad_dialog_window import Add_pointLoad_dialog_window
from Ui.Rectangular_cross_section_dialog_window import Rectangular_cross_section_dialog_window
from Ui.Square_cross_section_dialog_window import Square_cross_section_dialog_window
from Calculator.Material import SteelAISI1045, CastIronGrade20


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("/home/mark/Desktop/Beam Calculator/beamCalculator/Ui/uiFiles/beam_calculator_main_window.ui",self)

        self.crossSectionComboBoxDialogWindowMappings = {0: None,
                                                         1: self.open_square_cross_section_dialog_window,
                                                         2: self.open_rectangular_cross_section_dialog_window}
        self.crossSection = None
        self.materialMappings = {0: None, 1: SteelAISI1045, 2: CastIronGrade20}
        #Define click event actions for buttons
        self.AddBeamButton.clicked.connect(self.open_add_beam_window)
        self.AddPointLoadButton.clicked.connect(self.open_add_pointLoad_window)
        self.AddSupportButton.clicked.connect(self.open_add_support_window)
        self.CrossSectionSelectionComboBox.currentIndexChanged.connect(self.open_cross_section_dialog_window)


    def open_add_beam_window(self): #Group into one open_dialog_window function with a dialog.uiFiles parameter
        dialog = Add_beam_dialog_window()
        dialog.exec_()
        dialog.show()

    def open_add_support_window(self):
        dialog = Add_support_dialog_window()
        dialog.exec_()
        dialog.show()

    def open_add_pointLoad_window(self):
        dialog = Add_pointLoad_dialog_window()
        dialog.exec_()
        dialog.show()

    def open_cross_section_dialog_window(self):
        idx = self.CrossSectionSelectionComboBox.currentIndex()
        self.crossSectionComboBoxDialogWindowMappings[idx]()


    def open_rectangular_cross_section_dialog_window(self):
        dialog = Rectangular_cross_section_dialog_window()
        dialog.exec_()
        dialog.show()
        self.crossSection = dialog.get_user_cross_section()

    def open_square_cross_section_dialog_window(self):
        dialog = Square_cross_section_dialog_window()
        dialog.exec_()
        dialog.show()
        self.crossSection = dialog.get_user_cross_section()

    def get_selected_material(self):
        return self.materialMappings[self.materialSelectionComboBox.currentIndex()]()

    def get_selected_crossSection(self):
        pass







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec_())