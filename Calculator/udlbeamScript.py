import traceback

from matplotlib import pyplot as plt
import numpy as np
from sympy import *
x = symbols("x")
from beamCalculator.Calculator.Beam.Beam import Beam
from beamCalculator.Calculator.CrossSection.SquareCrossSection import SquareCrossSection
from beamCalculator.Calculator.Material.SteelAISI1045 import SteelAISI1045


def main():
    test_beam = Beam(1, SquareCrossSection(0.1), SteelAISI1045())
    test_beam.add_roller_support(0)
    test_beam.add_pin_support(1)
    test_beam.add_point_load(100, 0.5)
    test_beam.add_moment(-100, 0.1)
    test_beam.add_udl(100, 0.5, 1, 0)

    try:
        test_beam.calculate()
        test_beam.sympy_beam.plot_bending_moment()
        test_beam.sympy_beam.plot_shear_force()
        test_beam.sympy_beam.plot_deflection()
        fbd = test_beam.sympy_beam.draw()
        fbd.show()
        test_beam.symbeam_beam.plot()
        plt.show()
    except:
        traceback.print_exc()


if __name__ == '__main__':
    main()