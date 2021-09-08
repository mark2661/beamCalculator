import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets, uic

class Solution_summary_dialog_window(QtWidgets.QDialog):
    def __init__(self, user_beam):
        super(Solution_summary_dialog_window, self).__init__()
        uic.loadUi("/home/mark/Desktop/Beam Calculator/beamCalculator/Ui/UiFiles/Solution_summary_dialog_window.ui", self)
        self.user_beam = user_beam

        #Connect buttons to functions
        self.Ok_button.clicked.connect(self.close)
        self.BMPlot_button.clicked.connect(self.show_BM_plot)
        self.SFPlot_button.clicked.connect(self.show_SF_plot)
        self.DeflectionPlotButton.clicked.connect(self.show_Deflection_plot)
        self.FBDPlot_button.clicked.connect(self.show_FBD_plot)
        self.GenerateReport_button.clicked.connect(self.generate_report)

        #set label text
        #self.maxBendingMomentLabel.setText(str(round(float(self.user_beam.maxBM), 2)))
        self.maxShearForceLabel.setText(str(round(float(self.user_beam.maxSF), 2)))
        self.maxDeflectionLabel.setText(str(round(float(self.user_beam.maxDeflection), 2)))

    def show_FBD_plot(self):
        fbd = self.user_beam.sympy_beam.draw()
        fbd.show()

    def show_BM_plot(self):
        self.user_beam.sympy_beam.plot_bending_moment()

    def show_SF_plot(self):
        self.user_beam.sympy_beam.plot_shear_force()

    def show_Deflection_plot(self):
        self.user_beam.sympy_beam.plot_deflection()

    def generate_report(self):
        self.user_beam.symbeam_beam.plot()
        plt.show()
