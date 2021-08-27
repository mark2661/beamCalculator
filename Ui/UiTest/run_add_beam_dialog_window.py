from PyQt5 import QtWidgets
import sys
#from Ui.Add_beam_dialog_window import Add_beam_dialog_window
from beamCalculator.Ui.Add_beam_dialog_window import Add_beam_dialog_window


def run():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Add_beam_dialog_window()
    MainWindow.show()
    app.exec_()
    # sys.exit(app.exec_())

run()