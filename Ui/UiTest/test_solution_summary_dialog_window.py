import unittest, pyautogui, sys, pytestqt

import pytest, time, concurrent.futures
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox

from beamCalculator.Calculator.CrossSection.SquareCrossSection import SquareCrossSection
from beamCalculator.Calculator.Material.SteelAISI1045 import SteelAISI1045
from beamCalculator.Ui.Solution_summary_dialog_window import Solution_summary_dialog_window
from beamCalculator.Calculator.Beam.Beam import Beam


@pytest.fixture
def window(qtbot):
    class MockUserBeam:
        def __init__(self):
            self.beam = Beam(1, SquareCrossSection(0.1), SteelAISI1045())
            self.beam.set_loads([("point", 100.0, 0.5)])
            self.beam.set_supports([("pin", 0.0), ("roller", 1)])
            self.beam.calculate()
    window = Solution_summary_dialog_window(MockUserBeam().beam)
    window.show()
    qtbot.addWidget(window)
    return window

@pytest.mark.parametrize(
    'maxBM, maxSF, maxDeflection', [
        (25, 50, 1219.51), #int input
        # ('100.0', 100.0, float), #float input
        # ('one hundred', None, type(None)), #string input
        # ('1 hundred', None, type(None)), #mixed incorrect data type input
        # ('-100', None, type(None)), # negative input
        # ('', None, type(None)), #empty input
        # (None, None, type(None)) # NoneType input
    ]
)
def test_init(maxBM, maxSF, maxDeflection, window, qtbot):

    print(window.maxBendingMomentLabel.text(), window.maxShearForceLabel.text(), window.maxDeflectionLabel.text())
    #Assert
    assert float(window.maxShearForceLabel.text()) == maxSF
    #assert float(window.maxBendingMomentLabel.text()) == maxBM
    assert float(window.maxDeflectionLabel.text()) == maxDeflection

