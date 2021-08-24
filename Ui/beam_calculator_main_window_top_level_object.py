from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Add_beam_dialog_window import Add_beam_dialog_window
from Add_support_dialog_window import Add_support_dialog_window
from Add_pointLoad_dialog_window import Add_pointLoad_dialog_window

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi(".uiFiles/beam_calculator_main_window..uiFiles",self)
        #Define click event actions for buttons
        self.AddBeamButton.clicked.connect(self.open_add_beam_window)
        self.AddPointLoadButton.clicked.connect(self.open_add_pointLoad_window)
        self.AddSupportButton.clicked.connect(self.open_add_support_window)

    def open_add_beam_window(self): #Group into one open_dialog_window function with a dialog..uiFiles parameter
        dialog = Add_beam_dialog_window()
        dialog.exec_()
        dialog.show()

    def open_add_support_window(self):
        dialog = Add_support_dialog_window()
        dialog.exec_()
        dialog.show()

    def open_add_pointLoad_window(self):
        dialog = Add_pointLoad_dialog_window()
        dialog.exec_()
        dialog.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec_())