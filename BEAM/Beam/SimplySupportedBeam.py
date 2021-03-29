from abc import ABC

from BEAM.Beam.Beam import Beam
from BEAM.Support.PinSupport import PinSupport
from BEAM.Support.RollerSupport import RollerSupport


class SimplySupportedBeam(Beam, ABC):

    def __init__(self, length, cross_section, material):
        super.__init__(length, cross_section, material)

    def add_support(self, type, location):
        if type.lower() == "pin":
            self.add_pin_support(location)

        elif type.lower() == "roller":
            self.add_roller_support(location)

    def add_pin_support(self, location):
        new_pin_support = PinSupport(location)
        self.supports.append(new_pin_support)

    def add_roller_support(self, location):
        new_roller_support = RollerSupport(location)
        self.supports.append(new_roller_support)

    def calculate(self):


