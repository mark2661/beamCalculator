import unittest, pyautogui, sys, pytestqt

import pytest, time, concurrent.futures
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox

from beamCalculator.Ui.Add_UDL_dialog_window import Add_UDL_dialog_window

class TestAddPointLoadDialogWindow:
    @pytest.fixture
    def window(self, qtbot):
        window = Add_UDL_dialog_window()
        window.show()
        qtbot.addWidget(window)
        return window

    @pytest.mark.parametrize(
        'direction, inputLoadMagnitudeValue, inputLoadStartLocation, inputLoadEndLocation, inputLoadOrder, expectedDirection, expectedLoadMagnitude, expectedLoadStartLocation, expectedLoadEndLocation, expectedLoadOrder, expectedLoadMagnitudeType, expectedLoadStartLocationType, expectedLoadEndLocationType, expectedLoadOrderType', [
            ('down', "100", "0.5", "1.0", "0", -1, -100.0, 0.5, 1.0, 0, float, float, float, int), #int input
            # ('down', "100.0", "100.0", -1, -100.0, 100.0, float, float), #float input
            # ('down', "one hundred", "one hundred", -1, None, None, type(None), type(None)), #string input
            # ('down', "1 hundred", "1 hundred", -1, None, None, type(None), type(None)), #mixed incorrect data type input
            # ('down', "-100", "100", -1, None, None, type(None), type(None)), # negative magnitude
            # ('down', "100", "-100", -1, None, None, type(None), type(None)), # negative location
            # ('down', "", "100", -1, None, None, type(None), type(None)), #empty magnitude input
            # ('down', "100", "", -1, None, None, type(None), type(None)), #empty load input
            # ('down', None, None, -1, None, None, type(None), type(None)) # NoneType input
            #test location not on beam
        ]
    )
    def test_get_dialog_data(self, direction, inputLoadMagnitudeValue, inputLoadStartLocation, inputLoadEndLocation, inputLoadOrder,
                             expectedDirection, expectedLoadMagnitude, expectedLoadStartLocation, expectedLoadEndLocation, expectedLoadOrder,
                             expectedLoadMagnitudeType, expectedLoadStartLocationType, expectedLoadEndLocationType, expectedLoadOrderType,
                             window, qtbot):
        #Arrage
        def close_message_box():
            time.sleep(0.5)
            if type(QApplication.activeWindow()) is QMessageBox:
                QApplication.activeWindow().accept()
        """ Inorder to automatically close the error message window, a thread is created which checks if the error message window
        is active. If it is the window is closed and the test can continue in the dialog window.
        """
        #Action
        qtbot.keyClicks(window.loadDirectionComboBox, direction)
        qtbot.keyClicks(window.loadMagnitudeInputField, inputLoadMagnitudeValue)
        qtbot.keyClicks(window.loadStartLocationInputField, inputLoadStartLocation)
        qtbot.keyClicks(window.loadEndLocationInputField, inputLoadEndLocation)
        qtbot.keyClicks(window.loadOrderInputField, inputLoadOrder)
        executor = concurrent.futures.ThreadPoolExecutor().submit(close_message_box)
        qtbot.mouseClick(window.Ok_button, QtCore.Qt.LeftButton)
        #Assert
        assert window.inputted_load_direction == expectedDirection
        assert window.inputted_load_magnitude == expectedLoadMagnitude
        assert window.inputted_load_start_location == expectedLoadStartLocation
        assert window.inputted_load_end_location == expectedLoadEndLocation
        assert window.inputted_load_order == expectedLoadOrder
        assert type(window.inputted_load_magnitude) == expectedLoadMagnitudeType
        assert type(window.inputted_load_start_location) == expectedLoadStartLocationType
        assert type(window.inputted_load_end_location) == expectedLoadEndLocationType
        assert type(window.inputted_load_order) == expectedLoadOrderType

        executor.cancel()  # close the thread

def main():
    TestAddPointLoadDialogWindow()

if __name__ == "__main__":
    main()