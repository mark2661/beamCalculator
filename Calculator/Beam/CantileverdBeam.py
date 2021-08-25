from abc import ABC

from Calculator.Beam.Beam import Beam
from Calculator.Support.FixedSupport import FixedSupport
from Calculator.Support.PinSupport import PinSupport
from Calculator.Support.RollerSupport import RollerSupport


class CantileveredBeam(Beam, ABC):

    def __init__(self, length, cross_section, material):
        Beam.__init__(self, length, cross_section, material)
        self.supports = [FixedSupport(0)]


    def add_support(self, type_of_support, location):
        if type_of_support.lower() == "pin":
            self.add_pin_support(location)

        elif type_of_support.lower() == "roller":
            self.add_roller_support(location)

        elif type_of_support.lower() == "fixed":
            self.add_fixed_suport(location)

    def add_pin_support(self, location):
        new_pin_support = PinSupport(location)
        self.supports.append(new_pin_support)

    def add_roller_support(self, location):
        new_roller_support = RollerSupport(location)
        self.supports.append(new_roller_support)

    def add_fixed_support(self,location):
        new_fixed_support = FixedSupport(location)
        self.supports.append(new_fixed_support)