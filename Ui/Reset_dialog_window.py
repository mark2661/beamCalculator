from PyQt5 import QtCore, QtGui, QtWidgets, uic

class Reset_dialog_window(QtWidgets.QDialog):
    def __init__(self, mainWindow):
        super(Reset_dialog_window, self).__init__()
        uic.loadUi("/home/mark/Desktop/Beam Calculator/beamCalculator/Ui/UiFiles/Reset_dialog_window.ui", self)
        self.mainWindow = mainWindow
        self.check_box_to_reset_function_mappings = {self.resetBeamLength_checkBox: self.resetBeamLength,
                                                     self.resetSupports_checkBox: self.resetSupports,
                                                     self.resetPointLoads_checkBox: self.resetPointLoads,
                                                     self.resetMoments_checkBox: self.resetMoments,
                                                     self.resetUDL_checkBox: self.resetUDL,
                                                     self.resetMaterial_checkBox: self.resetMaterial,
                                                     self.resetCrossSection_checkBox: self.resetCrossSection}

        #connect buttons to functions
        self.resetAll_pushButton.clicked.connect(self.resetAll)
        self.resetSelected_pushButton.clicked.connect(self.resetSelected)

    def resetBeamLength(self):
        self.mainWindow.clear_user_beam_length()

    def resetSupports(self):
        self.mainWindow.clear_user_beam_supports()

    def resetPointLoads(self):
        self.mainWindow.clear_user_beam_point_loads()

    def resetMoments(self):
        pass

    def resetUDL(self):
        pass

    def resetMaterial(self):
        self.mainWindow.clear_user_beam_material()

    def resetCrossSection(self):
        self.mainWindow.clear_user_beam_cross_section()


    def resetAll(self):
        for check_box in self.check_box_to_reset_function_mappings.keys():
            self.check_box_to_reset_function_mappings[check_box]()
        self.close()

    def resetSelected(self):
        for check_box in self.check_box_to_reset_function_mappings.keys():
            if check_box.isChecked():
                self.check_box_to_reset_function_mappings[check_box]()
        self.close()