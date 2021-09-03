from unittest import mock
import pytest, time, concurrent.futures
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox
from beamCalculator.Calculator.CrossSection.RectangularCrossSection import RectangularCrossSection
from beamCalculator.Calculator.CrossSection.SquareCrossSection import SquareCrossSection
from beamCalculator.Calculator.Material.SteelAISI1045 import SteelAISI1045
from beamCalculator.Ui.beam_calculator_main_window import Window
from beamCalculator.Calculator.Beam.Beam import Beam

@pytest.fixture
def window(qtbot):
    window = Window()
    window.show()
    qtbot.addWidget(window)
    return window

@pytest.mark.parametrize(
    'inputttedBeamLength, expectedBeamLength, expectedBeamLengthType', [
        ('100', 100.0, float), #int input
        (None, None, type(None)) # NoneType input
    ]
)
def test_open_add_beam_window(inputttedBeamLength, expectedBeamLength, expectedBeamLengthType, window, qtbot):
    class MockAddBeamWindow(object):
        def __init__(self, inputtedBeamLength):
            try:
                self.inputted_beam_length = float(inputtedBeamLength)
            except:
                self.inputted_beam_length = None

        def exec_(self):
            pass

        def show(self):
            pass

    with mock.patch('beamCalculator.Ui.beam_calculator_main_window.Add_beam_dialog_window', return_value = MockAddBeamWindow(inputttedBeamLength)):
        #Action
        qtbot.mouseClick(window.addBeamButton, QtCore.Qt.LeftButton)
        assert window.user_beam_length == expectedBeamLength
        assert type(window.user_beam_length) == expectedBeamLengthType

@pytest.mark.parametrize(
    'inputtedSupportType, inputtedSupportLocation,  expectedResult', [
        ('pin', "100.0", [('pin', 100.0)]), #int input
        (None, None, []) # NoneType input
    ]
)
def test_open_add_support_window(inputtedSupportType, inputtedSupportLocation, expectedResult, window, qtbot):
    class MockAddSupportWindow(object):
        def __init__(self, inputtedSupportType, inputtedSupportLocation):
            self.support_type = inputtedSupportType
            try:
                self.support_location = float(inputtedSupportLocation)
            except:
                self.support_location = None

        def exec_(self):
            pass

        def show(self):
            pass

    with mock.patch('beamCalculator.Ui.beam_calculator_main_window.Add_support_dialog_window', return_value=MockAddSupportWindow(inputtedSupportType, inputtedSupportLocation)):
        #Action
        qtbot.mouseClick(window.addSupportButton, QtCore.Qt.LeftButton)
        assert window.user_beam_supports == expectedResult

@pytest.mark.parametrize(
    'inputtedDirection, inputtedLoadMagnitude, inputtedLoadLocation, expectedResult', [
        ('Up','100','100',[('point',100.0,100.0)]), #int input
        ('Up',None, None, []) # NoneType input
    ]
)
def test_open_add_pointLoad_window(inputtedDirection, inputtedLoadMagnitude, inputtedLoadLocation, expectedResult, window, qtbot):
    class MockAddPointLoadWindow(object):
        def __init__(self, inputtedDirection, inputtedLoadMagnitude, inputtedLoadLocation):
            self.inputted_load_direction = 1 if inputtedDirection == "Up" else -1
            try:
                self.inputted_load_magnitude = float(inputtedLoadMagnitude)
                self.inputted_load_location = float(inputtedLoadLocation)
                self.inputted_load_magnitude *= self.inputted_load_direction
            except:
                self.inputted_load_magnitude = self.inputted_load_location = None

        def exec_(self):
            pass

        def show(self):
            pass

    with mock.patch('beamCalculator.Ui.beam_calculator_main_window.Add_pointLoad_dialog_window', return_value=MockAddPointLoadWindow(inputtedDirection, inputtedLoadMagnitude, inputtedLoadLocation)):
        #Action
        qtbot.mouseClick(window.addPointLoadButton, QtCore.Qt.LeftButton)
        assert window.user_beam_loads == expectedResult

@pytest.mark.parametrize(
    'inputtedWidth, inputtedLength, expectedResultType, expectedResultWidth, expectedResultLength', [
        ('100.0', '100.0', RectangularCrossSection(100.0,100.0), 100.0, 100.0), #correct input
        #('Up',None, None, []) # NoneType input
    ]
)
def test_open_rectangular_cross_section_dialog_window(inputtedWidth, inputtedLength, expectedResultType, expectedResultWidth, expectedResultLength, window, qtbot):
    class MockRectangularCrossSectionWindow(object):
        def __init__(self, inputtedWidth, inputtedLength):

            try:
                width, length = inputtedWidth, inputtedLength
                if lambda width, length: float(width) > 0 and float(length) > 0:
                    self.cross_section_width = float(width)
                    self.cross_section_length = float(length)
                    self.user_cross_section = RectangularCrossSection(self.cross_section_width, self.cross_section_length)
            except:
                self.user_cross_section = None

        def exec_(self):
            pass

        def show(self):
            pass

        def get_user_cross_section(self):
            return self.user_cross_section

    with mock.patch('beamCalculator.Ui.beam_calculator_main_window.Rectangular_cross_section_dialog_window', return_value=MockRectangularCrossSectionWindow(inputtedWidth, inputtedLength)):
        #Action
        qtbot.mouseClick(window.crossSectionSelectionComboBox, QtCore.Qt.LeftButton)
        qtbot.keyClicks(window.crossSectionSelectionComboBox, "Rectangular")
        qtbot.keyClicks(window.crossSectionSelectionComboBox, "QtCore.Qt.Key_Enter")
        assert type(window.user_beam_cross_section) == type(expectedResultType)
        if window.user_beam_cross_section:
            assert window.user_beam_cross_section.width == expectedResultWidth
            assert window.user_beam_cross_section.height == expectedResultLength


@pytest.mark.parametrize(
    'inputtedLength, expectedResultType, expectedResultLength', [
        ('100.0', SquareCrossSection(100.0), 100.0), #correct input
        (None, None, None) # NoneType input
    ]
)
def test_open_square_cross_section_dialog_window(inputtedLength, expectedResultType, expectedResultLength, window, qtbot):
    class MockSquareCrossSectionWindow(object):
        def __init__(self,inputtedLength):

            try:
                length = inputtedLength
                if lambda length: float(length) > 0:
                    self.cross_section_length = float(length)
                    self.user_cross_section = SquareCrossSection(self.cross_section_length)
            except:
                self.user_cross_section = None

        def exec_(self):
            pass

        def show(self):
            pass

        def get_user_cross_section(self):
            return self.user_cross_section

    with mock.patch('beamCalculator.Ui.beam_calculator_main_window.Square_cross_section_dialog_window', return_value=MockSquareCrossSectionWindow(inputtedLength)):
        #Action
        qtbot.mouseClick(window.crossSectionSelectionComboBox, QtCore.Qt.LeftButton)
        qtbot.keyClicks(window.crossSectionSelectionComboBox, "Square")
        qtbot.keyClicks(window.crossSectionSelectionComboBox, "QtCore.Qt.Key_Enter")
        assert type(window.user_beam_cross_section) == type(expectedResultType)
        if window.user_beam_cross_section:
            assert window.user_beam_cross_section.height == expectedResultLength

@pytest.mark.parametrize(
    'inputtedMaterial, expectedResultType', [
        ('Steel', SteelAISI1045()), #correct input
        (None, None) # NoneType input
    ]
)
def test_get_selected_material(inputtedMaterial, expectedResultType, window, qtbot):
    #Action
    qtbot.keyClicks(window.materialSelectionComboBox, inputtedMaterial)
    qtbot.keyClicks(window.materialSelectionComboBox, "QtCore.Qt.Key_Enter")
    #Assert
    assert type(window.get_selected_material()) == type(expectedResultType)


@pytest.mark.skip()
@pytest.mark.parametrize(
    'inputtedMaterial, expectedResultType', [
        ('Steel', SteelAISI1045()), #correct input
        (None, None) # NoneType input
    ]
)
def test_get_selected_crossSection(inputtedMaterial, expectedResultType, window, qtbot):
    pass

@pytest.mark.parametrize(
    'inputtedBeamLength, inputtedBeamLoads, inputtedBeamSupports, inputtedBeamCrossSection, inputtedMaterial', [
        ('1', [("point", 100.0, 0.5)], [("pin", 0.0), ("roller", 1)], SquareCrossSection(0.1), SteelAISI1045), #correct input
        #(None, None) # NoneType input
    ]
)
def test_isValidBeamInput(inputtedBeamLength, inputtedBeamLoads, inputtedBeamSupports, inputtedBeamCrossSection, inputtedMaterial, window, qtbot):
    #Arrage
    def mock_get_selected_material():
        return inputtedMaterial()

    #monkey path get_selected_material function
    window.get_selected_material = mock_get_selected_material


    window.user_beam_length = inputtedBeamLength
    window.user_beam_loads = inputtedBeamLoads
    window.user_beam_supports = inputtedBeamSupports
    window.user_beam_cross_section = inputtedBeamCrossSection

    #Action
    window.isValidBeamInput()





@pytest.mark.parametrize(
    'inputtedBeamLength, inputtedBeamLoads, inputtedBeamSupports, inputtedBeamCrossSection, inputtedMaterial', [
        ('1', [("point", 100.0, 0.5)], [("pin", 0.0), ("roller", 1)], SquareCrossSection(0.1), SteelAISI1045), #correct input
        #(None, None) # NoneType input
    ]
)
def test_solve(inputtedBeamLength, inputtedBeamLoads, inputtedBeamSupports, inputtedBeamCrossSection, inputtedMaterial, window, qtbot):
    #Arrage
    def mock_get_selected_material():
        return inputtedMaterial()

    #monkey path get_selected_material function
    window.get_selected_material = mock_get_selected_material


    window.user_beam_length = inputtedBeamLength
    window.user_beam_loads = inputtedBeamLoads
    window.user_beam_supports = inputtedBeamSupports
    window.user_beam_cross_section = inputtedBeamCrossSection
    assert window.user_beam == None
    #Action
    qtbot.mouseClick(window.solveButton, QtCore.Qt.LeftButton)
    #Assert
    assert type(window.user_beam) == Beam
    assert window.user_beam.load_function != None
    assert window.user_beam.bending_moment_function != None
    assert window.user_beam.shear_force_function != None
    assert window.user_beam.deflection_function != None
    assert window.user_beam.free_body_diagram != None
    window.user_beam.free_body_diagram.show()
