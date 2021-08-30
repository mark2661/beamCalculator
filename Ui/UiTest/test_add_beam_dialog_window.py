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

def test_get_dialog_data_correct_input(window, qtbot):
    #Arrage
    qtbot.keyClicks(window.BeamLengthInputField, "100")
    #Action
    qtbot.mouseClick(window.Ok_button, QtCore.Qt.LeftButton)
    #Assert
    assert window.inputted_beam_length == 100.0
    assert type(window.inputted_beam_length) == float


def test_get_dialog_data_incorrect_input(window, qtbot):

    #Arrange
    def close_message_box():
        time.sleep(0.5)
        if type(QApplication.activeWindow()) is QMessageBox:
            QApplication.activeWindow().accept()
    """ Inorder to automatically close the error message window, a thread is created which checks if the error message window
    is active. If it is the window is closed and the test can continue in the dialog window.
    """
    #Action
    qtbot.keyClicks(window.BeamLengthInputField, "one hundred")
    executor = concurrent.futures.ThreadPoolExecutor().submit(close_message_box)
    qtbot.mouseClick(window.Ok_button, QtCore.Qt.LeftButton)

    #Assert
    assert window.inputted_beam_length == None

    executor.cancel() # close the thread







