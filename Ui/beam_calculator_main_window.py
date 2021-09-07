import traceback

from PyQt5 import QtWidgets, uic
from beamCalculator.Ui.Add_beam_dialog_window import Add_beam_dialog_window
from beamCalculator.Ui.Add_support_dialog_window import Add_support_dialog_window
from beamCalculator.Ui.Add_pointLoad_dialog_window import Add_pointLoad_dialog_window
from beamCalculator.Ui.Rectangular_cross_section_dialog_window import Rectangular_cross_section_dialog_window
from beamCalculator.Ui.Show_dialog_error_messgae_box import showDialogErrorMessageBox
from beamCalculator.Ui.Solution_summary_dialog_window import Solution_summary_dialog_window
from beamCalculator.Ui.Square_cross_section_dialog_window import Square_cross_section_dialog_window
from beamCalculator.Calculator.Material.SteelAISI1045 import SteelAISI1045
from beamCalculator.Calculator.Material.CastIronGrade20 import CastIronGrade20
from beamCalculator.Calculator.Beam.Beam import Beam



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("/home/mark/Desktop/Beam Calculator/beamCalculator/Ui/UiFiles/beam_calculator_main_window.ui",self)

        self.crossSectionComboBoxDialogWindowMappings = {0: None,
                                                         1: self.open_square_cross_section_dialog_window,
                                                         2: self.open_rectangular_cross_section_dialog_window}
        self.materialMappings = {0: None, 1: SteelAISI1045, 2: CastIronGrade20}

        #Properties of the users beam used for calculation
        self.user_beam_cross_section = None
        self.user_beam_length = None
        self.user_beam_loads = []
        self.user_beam_supports = []

        #Users beam object
        self.user_beam = None

        #Define click event actions for buttons
        self.addBeamButton.clicked.connect(self.open_add_beam_window)
        self.addPointLoadButton.clicked.connect(self.open_add_pointLoad_window)
        self.addSupportButton.clicked.connect(self.open_add_support_window)
        self.crossSectionSelectionComboBox.currentIndexChanged.connect(self.open_cross_section_dialog_window)
        self.solveButton.clicked.connect(self.solve)


    def open_add_beam_window(self): #Group into one open_dialog_window function with a dialog.UiFiles parameter
        dialog = Add_beam_dialog_window()
        dialog.exec_()
        dialog.show()
        self.user_beam_length = dialog.inputted_beam_length

    def open_add_support_window(self):
        dialog = Add_support_dialog_window()
        dialog.exec_()
        dialog.show()
        if dialog.support_type is not None and dialog.support_location is not None:
            self.user_beam_supports.append((dialog.support_type, dialog.support_location))

    def open_add_pointLoad_window(self):
        dialog = Add_pointLoad_dialog_window()
        dialog.exec_()
        dialog.show()
        if dialog.inputted_load_location and dialog.inputted_load_magnitude:
            self.user_beam_loads.append(("point", dialog.inputted_load_magnitude, dialog.inputted_load_location))

    def open_cross_section_dialog_window(self):
        idx = self.crossSectionSelectionComboBox.currentIndex()
        self.crossSectionComboBoxDialogWindowMappings[idx]()


    def open_rectangular_cross_section_dialog_window(self):
        dialog = Rectangular_cross_section_dialog_window()
        dialog.exec_()
        dialog.show()
        self.user_beam_cross_section = dialog.get_user_cross_section()

    def open_square_cross_section_dialog_window(self):
        dialog = Square_cross_section_dialog_window()
        dialog.exec_()
        dialog.show()
        self.user_beam_cross_section = dialog.get_user_cross_section()

    def open_solution_summary_dialog_window(self):
        dialog = Solution_summary_dialog_window(self.user_beam)
        dialog.exec_()
        dialog.show()

    def get_selected_material(self):
        try:
            return self.materialMappings[self.materialSelectionComboBox.currentIndex()]()
        except:
            return None

    def get_selected_crossSection(self):
        pass

    def solve(self):
        try:
            if self.isValidBeamInput():
                self.user_beam = Beam(self.user_beam_length, self.user_beam_cross_section, self.get_selected_material())
                self.user_beam.set_supports(self.user_beam_supports)
                self.user_beam.set_loads(self.user_beam_loads)
                self.user_beam.calculate()
                self.open_solution_summary_dialog_window()
            else:
                raise InvalidBeamInputException
        except:
            #traceback.print_exc()
            showDialogErrorMessageBox()

    def isValidBeamInput(self):
        if None in [self.user_beam_length, self.user_beam_cross_section, self.get_selected_material()] or len(self.user_beam_loads) == 0 or len(self.user_beam_supports) == 0:
            return False
        return True


class InvalidBeamInputException(Exception):
    pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec_())