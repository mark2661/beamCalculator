import unittest, pyautogui, sys, pytestqt

import pytest
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from beamCalculator.Ui.Add_beam_dialog_window import Add_beam_dialog_window

@pytest.fixture
def window(qtbot):
    window = Add_beam_dialog_window()
    window.show()
    qtbot.addWidget(window)
    return window

def test_get_dialog_data(window, qtbot):
    qtbot.keyClicks(window.BeamLengthInputField, "hello")
    qtbot.mouseClick(window.buttonBox.accepted(), QtCore.Qt.LeftButton)
    assert window.inputted_beam_length == "hello"




