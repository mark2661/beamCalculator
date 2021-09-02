import unittest, pyautogui, sys, pytestqt

import pytest, time, concurrent.futures
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox


from beamCalculator.Calculator.CrossSection.SquareCrossSection import SquareCrossSection
from beamCalculator.Ui.Square_cross_section_dialog_window import Square_cross_section_dialog_window


@pytest.fixture
def window(qtbot):
    window = Square_cross_section_dialog_window()
    window.show()
    qtbot.addWidget(window)
    return window

@pytest.mark.parametrize(
    'inputtedLength, expectedResultType, expectedResultLength', [
        ('100', SquareCrossSection(100.0), 100.0), #int input
        ('100.0', SquareCrossSection(100.0), 100.0), #float input
        ('one hundred', None, None), #string input
        ('1 hundred', None, None), #mixed incorrect data type input
        ('-100', None, None), # negative input
        ('', None, None), #empty input
        (None, None, None) # NoneType input
    ]
)
def test_get_dialog_data(inputtedLength, expectedResultType, expectedResultLength, window, qtbot):
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
    executor = concurrent.futures.ThreadPoolExecutor().submit(close_message_box)
    qtbot.mouseClick(window.Ok_button, QtCore.Qt.LeftButton)
    #Assert
    assert type(window.user_cross_section) == type(expectedResultType)
    if window.user_cross_section:
        assert window.user_cross_section.height == expectedResultLength
        assert window.user_cross_section.width == expectedResultLength

    executor.cancel()  # close the thread