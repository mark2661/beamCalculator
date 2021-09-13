import concurrent.futures
import time

import pytest
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox

from beamCalculator.Ui.Add_support_dialog_window import Add_support_dialog_window

class TestAddSupportDialogWindow:
    @pytest.fixture
    def window(self, qtbot):
        window = Add_support_dialog_window()
        window.show()
        qtbot.addWidget(window)
        return window

    @pytest.mark.parametrize(
        'inputSupportType, inputSupportLocation, expectedSupportType, expectedSupportLocation, expectedSupportLocationDataType', [
            ('pin', "50", 'pin', 50.0, float), #int input
            ('roller', "100.0", 'roller', 100.0, float), #float input
            ('roller', "one hundred", 'roller', None,  type(None)), #string input
            ('fixed', '1 hundred', 'fixed', None, type(None)), #mixed incorrect data type input
            ('pin', '-100', 'pin', None, type(None)), # negative input
            ('pin','', 'pin', None, type(None)), #empty input
            ('pin', None, 'pin', None, type(None)) # NoneType input
            # test location outside of beam length
        ]
    )
    def test_get_dialog_data(self, inputSupportType, inputSupportLocation, expectedSupportType, expectedSupportLocation, expectedSupportLocationDataType, window, qtbot):
        #Arrage
        def close_message_box():
            time.sleep(0.5)
            if type(QApplication.activeWindow()) is QMessageBox:
                QApplication.activeWindow().accept()
        """ Inorder to automatically close the error message window, a thread is created which checks if the error message window
        is active. If it is the window is closed and the test can continue in the dialog window.
        """
        #Action
        executor = concurrent.futures.ThreadPoolExecutor().submit(close_message_box)
        qtbot.keyClicks(window.supportTypeComboBox, inputSupportType)
        qtbot.keyClicks(window.supportLocationInputField, inputSupportLocation)
        qtbot.mouseClick(window.Ok_button, QtCore.Qt.LeftButton)
        #Assert
        assert window.support_type == expectedSupportType
        assert window.support_location == expectedSupportLocation
        assert type(window.support_location) == expectedSupportLocationDataType

        executor.cancel()  # close the thread

def main():
    TestAddSupportDialogWindow()

if __name__ == "__main__":
    main()