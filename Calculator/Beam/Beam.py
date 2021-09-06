from abc import ABC, abstractmethod

#from BEAM.Load.Moment import Moment
#from BEAM.Load.PointLoad import PointLoad
#from BEAM.Load.UDL import UDL
from sympy.physics.continuum_mechanics.beam import Beam as sympyBeam
from sympy import *
from itertools import chain

from beamCalculator.Calculator.Load.PointLoad import PointLoad
from beamCalculator.Calculator.Load.UDL import UDL
from beamCalculator.Calculator.Load.Moment import Moment
from beamCalculator.Calculator.Support.FixedSupport import FixedSupport
from beamCalculator.Calculator.Support.PinSupport import PinSupport
from beamCalculator.Calculator.Support.RollerSupport import RollerSupport


class Beam():

    def __init__(self, length, cross_section, material):
        self.length = length
        self.cross_section = cross_section
        self.material = material

        self.point_loads = []
        self.moments = []
        self.udl = []
        self.supports = []

        # self.load_function = None
        # self.bending_moment_function = None
        # self.shear_force_function = None
        # self.deflection_function = None
        # self.free_body_diagram = None
        self.sympy_beam = None

        self.maxBM, self.maxBMLocation = None, None
        self.maxSF, self.maxSFLocation = None, None
        self.maxDeflection, self.maxDeflectionLocation = None, None

        self.load_mappings = {"point": self.add_point_load, "moment":self.add_moment, "udl":self.add_udl}
        self.support_mappings = {"pin":self.add_pin_support, "roller":self.add_roller_support, "fixed":self.add_fixed_support}

    """
    ** GETTERS AND SETTERS **
    """
    def get_length(self):
        return self.length

    def get_cross_section(self):
        return self.cross_section

    def get_material(self):
        return self.material

    def set_length(self, length):
        self.length = length

    def set_cross_section(self, cross_section):
        self.cross_section = cross_section

    def set_loads(self, loads):
        for load in loads:
            self.add_load(*load)

    def set_supports(self, supports):
        for support in supports:
            self.add_support(*support)

    def set_load_function(self, function):
        self.load_function = function

    def set_bending_moment_function(self, function):
        self.bending_moment_function = function

    def set_shear_force_function(self, function):
        self.shear_force_function = function

    def set_deflection_function(self, function):
        self.deflection_function = function

    def set_free_body_diagram(self, plot_object):
        self.free_body_diagram = plot_object


    """
    ********************************
    """

    """
    ** FUNCTIONS FOR FORCES **
    """

    def add_load(self,type_of_load, magnitude, location, end_location=None):
        self.load_mappings[type_of_load](magnitude, location, end_location)

    def add_point_load(self,magnitude,location, *args):
        new_point_load = PointLoad(magnitude, location)
        self.point_loads.append(new_point_load)

    def add_moment(self,magnitude,location, *args):
        new_moment = Moment(magnitude,location)
        self.moments.append(new_moment)

    def add_udl(self,magnitude,start_location,end_location):
        new_udl = UDL(magnitude,start_location, end_location)
        self.moments.append(new_udl)

    def clear_loads(self):
        self.point_loads.clear()
        self.moments.clear()
        self.udl.clear()

    """
    **************************************
    """

    """
     ** FUNCTIONS FOR SUPPORTS **
    """
    def add_support(self, type_of_support, location):
        self.support_mappings[type_of_support](location)

    def add_pin_support(self, location):
        new_pin_support = PinSupport(location)
        self.supports.append(new_pin_support)

    def add_roller_support(self, location):
        new_roller_support = RollerSupport(location)
        self.supports.append(new_roller_support)

    def add_fixed_support(self, location):
        new_fixed_support = FixedSupport(location)
        self.supports.append(new_fixed_support)

    def clear_supports(self):
        self.supports.clear()

    """
    **************************************
    """

    def calculate(self):
        E = self.material.tensile_modulus
        I = self.cross_section.get_area_moment_of_inertia()

        beam = sympyBeam(self.length, E, I)
        beam.apply_support = apply_support_fix

        self.apply_loads_to_sympy_beam_object(beam)
        #self.apply_supports_to_sympy_beam_object(beam)
        beam.solve_for_reaction_loads(*self.make_reaction_symbols_for_sympy_beam_object(beam))


        # self.set_load_function(beam.load)
        # self.set_bending_moment_function(beam.bending_moment())
        # self.set_shear_force_function(beam.shear_force())
        # self.set_deflection_function(beam.deflection())
        # self.set_free_body_diagram(beam.draw())


        self.maxBM = beam.max_bmoment()[1]
        self.maxSF = beam.max_shear_force()[1]
        self.maxDeflection = beam.max_deflection()[1]
        self.sympy_beam = beam




    def apply_loads_to_sympy_beam_object(self, beam):
        for load in self.point_loads:
            beam.apply_load(load.magnitude, load.start_location, -1)

        for moment in self.moments:
            beam.apply_load(moment.magnitude, moment.start_location, -2)

        for udl in self.udl:
            beam.apply_load(udl.magnitude,udl.start_location,0, end=udl.end_location)

    # def apply_supports_to_sympy_beam_object(self, beam):
    #     for support in self.supports:
    #         beam.apply_support(beam, support.location, support.supportType)

    def make_reaction_symbols_for_sympy_beam_object(self, beam):
        reaction_symbols = []
        for support in self.supports:
            if support.supportType == "fixed":
                symbl = symbols('R_{0}, M_{0}'.format(support.location))
                reaction_symbols.extend(symbl)
                beam.apply_support(beam, symbl, support.location, support.supportType)
            else:
                symbl = symbols('R_{0}'.format(support.location))
                reaction_symbols.append(symbl)
                beam.apply_support(beam, symbl, support.location, support.supportType)
        return reaction_symbols


"""
Code from GitHub used to fix the issue where sympy beams would not accept decimal values for support locations
"""
def apply_support_fix(self, syms, loc, type="fixed"):
    try:
        reaction_load,reaction_moment = syms
    except:
        try:
            reaction_load, = syms
        except:
            reaction_load = syms
    loc = sympify(loc)
    self._applied_supports.append((loc, type))
    if type == "pin" or type == "roller":
        self.apply_load(reaction_load, loc, -1)
        self.bc_deflection.append((loc, 0))
    else:
        self.apply_load(reaction_load, loc, -1)
        self.apply_load(reaction_moment, loc, -2)
        self.bc_deflection.append((loc, 0))
        self.bc_slope.append((loc, 0))
        self._support_as_loads.append((reaction_moment, loc, -2, None))
    self._support_as_loads.append((reaction_load, loc, -1, None))

    """
    ** ABSTRACT METHODS **
    """
    # @abstractmethod
    # def calculate_max_moment(self):
    #     pass
    #
    # @abstractmethod
    # def calculate_moment_at_location_x(self,x):
    #     pass
    #
    # @abstractmethod
    # def calculate_max_deflection(self):
    #     pass
    #
    # @abstractmethod
    # def calculate_deflection_at_location_x(self,x):
    #     pass
    #
    # @abstractmethod
    # def calculate_max_shear_force(self):
    #     pass
    #
    # @abstractmethod
    # def calculate_shear_force_at_location_x(self,x):
    #     pass
    #
    # @abstractmethod
    # def calculate_support_reactions(self):
    #     pass

