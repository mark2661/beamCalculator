import unittest, pyautogui, sys, pytestqt
from unittest import mock

import pytest, time, concurrent.futures
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox

from beamCalculator.Calculator.CrossSection.SquareCrossSection import SquareCrossSection
from beamCalculator.Calculator.Material.SteelAISI1045 import SteelAISI1045
from beamCalculator.Ui.Reset_dialog_window import Reset_dialog_window
from beamCalculator.Ui.Solution_summary_dialog_window import Solution_summary_dialog_window
from beamCalculator.Calculator.Beam.Beam import Beam
from beamCalculator.Ui.beam_calculator_main_window import Window as MainWindow

class TestResetDialogWindow:
    @pytest.fixture
    def window(self, qtbot):

        # def MockMainWindow():
        #     mockMainWindow = MainWindow
        #     mockMainWindow.user_beam_length = 1
        #     mockMainWindow.user_beam_cross_section = SquareCrossSection(0.1)
        #     mockMainWindow.user_beam_loads = [("point", 100.0, 0.5)]
        #     mockMainWindow.user_beam_supports = [("pin", 0.0), ("roller", 1)]
        #     #mockMainWindow.crossSectionSelectionComboBox.setCurrentIndex(1)
        #     #mockMainWindow.materialSelectionComboBox.setCurrentIndex(1)
        #
        #     return mockMainWindow
        mmw = MainWindow()
        mmw.user_beam_length = 1
        mmw.user_beam_cross_section = SquareCrossSection(0.1)
        mmw.user_beam_loads = [("point", 100.0, 0.5), ("moment", 100.0, 0.1)]
        mmw.user_beam_supports = [("pin", 0.0), ("roller", 1)]
        #mockMainWindow.crossSectionSelectionComboBox.setCurrentIndex(1)
        #mockMainWindow.materialSelectionComboBox.setCurrentIndex(1)
        window = Reset_dialog_window(mmw)
        window.show()
        qtbot.addWidget(window)
        return window

    # @pytest.mark.parametrize(
    #     'maxBM, maxSF, maxDeflection', [
    #         (25, 50, 1219.51), #int input
    #         # ('100.0', 100.0, float), #float input
    #         # ('one hundred', None, type(None)), #string input
    #         # ('1 hundred', None, type(None)), #mixed incorrect data type input
    #         # ('-100', None, type(None)), # negative input
    #         # ('', None, type(None)), #empty input
    #         # (None, None, type(None)) # NoneType input
    #     ]
    # )
    def test_resetBeamLength(self, window, qtbot):
        print(type(window.mainWindow))
        assert window.mainWindow.user_beam_length != None
        window.resetBeamLength()
        assert window.mainWindow.user_beam_length == None


    def test_resetSupports(self, window, qtbot):

        assert window.mainWindow.user_beam_supports != []
        window.resetSupports()
        assert window.mainWindow.user_beam_supports == []


    def test_resetPointLoads(self, window, qtbot):

        assert window.mainWindow.user_beam_loads != []
        window.resetPointLoads()
        assert len(window.mainWindow.user_beam_loads) > 0
        for load in window.mainWindow.user_beam_loads:
            assert load[0] != 'point'

    def test_resetMoments(self, window, qtbot):

        assert window.mainWindow.user_beam_loads != []
        window.resetMoments()
        assert len(window.mainWindow.user_beam_loads) > 0
        for load in window.mainWindow.user_beam_loads:
            assert load[0] != 'moment'

    @pytest.mark.skip(reason="functionality to add UDL not implemented")
    def test_resetUDL(self, window, qtbot):

        assert window.user_beam.udl != []
        window.resetUDL()
        assert window.user_beam.udl == []

    @pytest.mark.skip(reason="functionality to add moments not yet tested")
    def test_resetMaterial(self, window, qtbot):

        assert window.user_beam.material != None
        window.resetMaterial()
        assert window.user_beam.material == None


    def test_resetCrossSection(self, window, qtbot):
        class MockCrossSectionSelectionComboBox:
            def __init__(self):
                pass
            def setCurrentIndex(self, val):
                pass
        #monkey patch for crossSectionSelectionComboBox class attribute
        window.mainWindow.crossSectionSelectionComboBox = MockCrossSectionSelectionComboBox()
        assert window.mainWindow.user_beam_cross_section != None
        window.resetCrossSection()
        assert window.mainWindow.user_beam_cross_section == None


    @pytest.mark.skip(reason="functionality to add moments not yet tested")
    def test_resetAll(self, window, qtbot):

        assert window.user_beam.length != None
        assert window.user_beam.cross_section != None
        assert window.user_beam.material != None
        assert window.user_beam.point_loads != []
        #assert window.user_beam.moments != []
        #assert window.user_beam.udl != []
        assert window.user_beam.supports != []

        #Action
        window.resetAll()


        assert window.user_beam.length == None
        assert window.user_beam.cross_section == None
        assert window.user_beam.material == None
        assert window.user_beam.point_loads == []
        # assert window.user_beam.moments == []
        # assert window.user_beam.udl == []
        assert window.user_beam.supports == []

    #@pytest.mark.skip(reason="functionality to add moments not yet tested")
    def test_resetSelected(self, window, qtbot):

        assert window.mainWindow.user_beam_length != None
        assert window.mainWindow.user_beam_cross_section != None
        #assert window.mainWindow.get_selected_material() != None
        assert window.mainWindow.user_beam_loads != []
        assert window.mainWindow.user_beam_supports != []

        #Action
        qtbot.mouseClick(window.resetCrossSection_checkBox, QtCore.Qt.LeftButton)
        #qtbot.mouseClick(window.resetMaterial_checkBox, QtCore.Qt.LeftButton)
        qtbot.mouseClick(window.resetPointLoads_checkBox, QtCore.Qt.LeftButton)
        qtbot.mouseClick(window.resetSupports_checkBox, QtCore.Qt.LeftButton)

        qtbot.mouseClick(window.resetSelected_pushButton, QtCore.Qt.LeftButton)


        #Assert
        assert window.mainWindow.user_beam_length != None #purposly not selected to change this to ensure everything isn't being reset
        assert window.mainWindow.user_beam_cross_section == None
        #assert window.mainWindow.get_selected_material() == None
        assert window.mainWindow.user_beam_supports == []
        for load in window.mainWindow.user_beam_loads:
            assert load[0] != 'point'

def main():
    TestResetDialogWindow()

if __name__ == "__main__":
    main()