from PyQt5 import QtCore, QtGui, QtWidgets, uic

#from beam_calculator_main_window import Ui_MainWindow

# from Add_beam_dialog_window import Ui_Dialog as Ui_add_beam_dialog, Add_beam_dialog_window
from Add_beam_dialog_window import Add_beam_dialog_window
from Add_support_dialog_window import Ui_Dialog as Ui_add_support_dialog
from Add_pointLoad_dialog_window import Ui_Dialog as Ui_add_pointLoad_dialog


# class Window(QtWidgets.QMainWindow):
#     def __init__(self):
#         QtWidgets.QMainWindow.__init__(self)
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         #Define click event actions for buttons
#         self.ui.AddBeamButton.clicked.connect(self.open_add_beam_window)
#         self.ui.AddPointLoadButton.clicked.connect(self.open_add_pointLoad_window)
#         self.ui.AddSupportButton.clicked.connect(self.open_add_support_window)
#
#     def open_add_beam_window(self): #Group into one open_dialog_window function with a dialog.ui parameter
#         dialog = QtWidgets.QDialog()
#         dialog.ui = Ui_add_beam_dialog()
#         dialog.ui.setupUi(dialog)
#         dialog.exec_()
#         dialog.show()
#
#     def open_add_support_window(self):
#         dialog = QtWidgets.QDialog()
#         dialog.ui = Ui_add_support_dialog()
#         dialog.ui.setupUi(dialog)
#         dialog.exec_()
#         dialog.show()
#
#     def open_add_pointLoad_window(self):
#         dialog = QtWidgets.QDialog()
#         dialog.ui = Ui_add_pointLoad_dialog()
#         dialog.ui.setupUi(dialog)
#         dialog.exec_()
#         dialog.show()

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("ui/beam_calculator_main_window.ui",self)
        #Define click event actions for buttons
        self.AddBeamButton.clicked.connect(self.open_add_beam_window)
        self.AddPointLoadButton.clicked.connect(self.open_add_pointLoad_window)
        self.AddSupportButton.clicked.connect(self.open_add_support_window)

    def open_add_beam_window(self): #Group into one open_dialog_window function with a dialog.ui parameter
        dialog = Add_beam_dialog_window()
        # dialog = QtWidgets.QDialog()
        # dialog.ui = Ui_add_beam_dialog()
        # dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def open_add_support_window(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_add_support_dialog()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def open_add_pointLoad_window(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_add_pointLoad_dialog()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec_())