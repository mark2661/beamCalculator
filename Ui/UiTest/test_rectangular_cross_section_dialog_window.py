import unittest, pyautogui, sys, pytestqt

import pytest, time, concurrent.futures
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox

from beamCalculator.Calculator.CrossSection.RectangularCrossSection import RectangularCrossSection
from beamCalculator.Ui.Rectangular_cross_section_dialog_window import Rectangular_cross_section_dialog_window


@pytest.fixture
def window(qtbot):
    window = Rectangular_cross_section_dialog_window()
    window.show()
    qtbot.addWidget(window)
    return window

@pytest.mark.parametrize(
    'inputtedWidth, inputtedLength, expectedResultType, expectedResultWidth, expectedResultLength', [
        ('100', '100', RectangularCrossSection(100.0, 100.0), 100.0, 100.0), #int input
        ('100.0', '100.0', RectangularCrossSection(100.0, 100.0), 100.0, 100.0), #float input
        ('one hundred', 'one hundred', None, None, None), #string input
        ('1 hundred', '1 hundred', None, None, None), #mixed incorrect data type input
        ('-100', '-100', None, None, None), # negative input
        ('', '', None, None, None), #empty input
        (None, None, None, None, None) # NoneType input
    ]
)
def test_get_dialog_data(inputtedWidth, inputtedLength, expectedResultType, expectedResultWidth, expectedResultLength, window, qtbot):
    #Arrage
    def close_message_box():
        time.sleep(0.5)
        if type(QApplication.activeWindow()) is QMessageBox:
            QApplication.activeWindow().accept()
    """ Inorder to automatically close the error message window, a thread is created which checks if the error message window
    is active. If it is the window is closed and the test can continue in the dialog window.
    """
    #Action
    qtbot.keyClicks(window.crossSectionLengthInputField, inputtedLength)
    qtbot.keyClicks(window.crossSectionWidthInputField, inputtedWidth)
    executor = concurrent.futures.ThreadPoolExecutor().submit(close_message_box)
    qtbot.mouseClick(window.Ok_button, QtCore.Qt.LeftButton)
    #Assert
    assert type(window.user_cross_section) == type(expectedResultType)
    if window.user_cross_section:
        assert window.user_cross_section.width == expectedResultWidth
        assert window.user_cross_section.height == expectedResultLength

    executor.cancel()  # close the thread