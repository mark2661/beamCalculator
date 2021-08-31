import unittest, pyautogui, sys, pytestqt

import pytest, time, concurrent.futures
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox

from beamCalculator.Ui.Add_beam_dialog_window import Add_beam_dialog_window, InputError

@pytest.fixture
def window(qtbot):
    window = Add_beam_dialog_window()
    window.show()
    qtbot.addWidget(window)
    return window

@pytest.mark.parametrize(
    'length, inputFieldValue, inputFieldType', [
        ('100', 100.0, float), #int input
        ('100.0', 100.0, float), #float input
        ('one hundred', None, type(None)), #string input
        ('1 hundred', None, type(None)), #mixed incorrect data type input
        ('-100', None, type(None)), # negative input
        ('', None, type(None)), #empty input
        (None, None, type(None)) # NoneType input
    ]
)
def test_get_dialog_data(length, inputFieldValue, inputFieldType, window, qtbot):
    #Arrage
    def close_message_box():
        time.sleep(0.5)
        if type(QApplication.activeWindow()) is QMessageBox:
            QApplication.activeWindow().accept()
    """ Inorder to automatically close the error message window, a thread is created which checks if the error message window
    is active. If it is the window is closed and the test can continue in the dialog window.
    """
    #Action
    qtbot.keyClicks(window.BeamLengthInputField, length)
    executor = concurrent.futures.ThreadPoolExecutor().submit(close_message_box)
    qtbot.mouseClick(window.Ok_button, QtCore.Qt.LeftButton)
    #Assert
    assert window.inputted_beam_length == inputFieldValue
    assert type(window.inputted_beam_length) == inputFieldType

    executor.cancel()  # close the thread

# @pytest.mark.skip()
# def test_get_dialog_data_incorrect_input(window, qtbot):
#
#     #Arrange
#     def close_message_box():
#         time.sleep(0.5)
#         if type(QApplication.activeWindow()) is QMessageBox:
#             QApplication.activeWindow().accept()
#     """ Inorder to automatically close the error message window, a thread is created which checks if the error message window
#     is active. If it is the window is closed and the test can continue in the dialog window.
#     """
#     #Action
#     qtbot.keyClicks(window.BeamLengthInputField, "one hundred")
#     executor = concurrent.futures.ThreadPoolExecutor().submit(close_message_box)
#     qtbot.mouseClick(window.Ok_button, QtCore.Qt.LeftButton)
#
#     #Assert
#     assert window.inputted_beam_length == None
#
#     executor.cancel() # close the thread







