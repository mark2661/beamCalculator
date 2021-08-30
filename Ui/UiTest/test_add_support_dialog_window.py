
import pytest
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from beamCalculator.Ui.Add_support_dialog_window import Add_support_dialog_window


@pytest.fixture
def window(qtbot):
    window = Add_support_dialog_window()
    window.show()
    qtbot.addWidget(window)
    return window

@pytest.mark.skip(reason="difficulty implmenting qtbot with the ui")
def test_get_dialog_data_correct_input(window, qtbot):
    #Arrage
    qtbot.keyClicks(window.supportTypeComboBox, "R")
    #Action
    qtbot.keyClick(window.supportTypeComboBox, QtCore.Qt.Key_Enter)
    qtbot.keyClicks(window.suppportLocationInputField, "100")
    qtbot.keyClick(window.suppportLocationInputField, QtCore.Qt.Key_Enter)

    #Assert
    assert window.support_type == "roller"
    assert type(window.support_type) == str

    assert window.support_location == 100.0
    assert type(window.support_location) == float

def test_get_dialog_data_correct_input():
    window = Add_support_dialog_window()
