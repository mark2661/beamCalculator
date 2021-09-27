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
        # bm = []
        # sf = []
        # de = []
        # #print(test_beam.sympy_beam.shear_force())
        # #print(type(float(test_beam.sympy_beam.bending_moment().subs(x, 0.5))))
        # for point in np.arange(0.001, test_beam.length, 0.001):
        #     bm_val = float(test_beam.sympy_beam.bending_moment().subs(x, point))
        #     sf_val = float(test_beam.sympy_beam.shear_force().subs(x, point))
        #     de_val = float(test_beam.sympy_beam.deflection().subs(x, point))
        #     if abs(bm_val) != float('inf'):
        #         bm.append(bm_val)
        #     if abs(sf_val) != float('inf'):
        #         sf.append(sf_val)
        #     if abs(de_val) != float('inf'):
        #         de.append(de_val)
        # print(max(bm), min(sf), max(de))
        # print(sf)
        #print(type(test_beam.sympy_beam.bending_moment().subs(x, 0.5)))
        #print(test_beam.sympy_beam.bending_moment().subs(x, 0.5))
        #test_beam.sympy_beam.plot_bending_moment()
    except:
        traceback.print_exc()


if __name__ == '__main__':
    main()