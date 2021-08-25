from abc import ABC, abstractmethod

#from BEAM.Load.Moment import Moment
#from BEAM.Load.PointLoad import PointLoad
#from BEAM.Load.UDL import UDL
from sympy.physics.continuum_mechanics.beam import Beam as sympyBeam
from sympy import *
from itertools import chain

from Calculator.Load.PointLoad import PointLoad
from Calculator.Load.UDL import UDL
from Calculator.Load.Moment import Moment


class Beam(ABC):

    def __init__(self, length, cross_section, material):
        self.length = length
        self.cross_section = cross_section
        self.material = material

        self.point_loads = []
        self.moments = []
        self.udl = []
        self.supports = []

        self.load_function = None
        self.bending_moment_function = None
        self.shear_force_function = None
        self.deflection_function = None
        self.free_body_diagram = None

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

    def set_material(self, material):
        self.material = material

    def set_load_function(self,function):
        self.load_function = function

    def set_bending_moment_function(self,function):
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
    def add_point_load(self,magnitude,location):
        new_point_load = PointLoad(magnitude, location)
        self.point_loads.append(new_point_load)

    def add_moment(self,magnitude,location):
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

    def clear_supports(self):
        self.supports.clear()

    """
    **************************************
    """

    def calculate(self):
        E = self.material.tensile_modulus
        I = self.cross_section.get_area_moment_of_inertia()

        beam = sympyBeam(self.length, E, I)
        self.apply_loads_to_sympy_beam_object(beam)
        self.apply_supports_to_sympy_beam_object(beam)
        beam.solve_for_reaction_loads(*self.make_reaction_symbols_for_sympy_beam_object(beam))


        self.set_load_function(beam.load)
        self.set_bending_moment_function(beam.bending_moment())
        self.set_shear_force_function(beam.shear_force())
        self.set_deflection_function(beam.deflection())
        self.set_free_body_diagram(beam.draw())


    def apply_loads_to_sympy_beam_object(self, beam):
        for load in self.point_loads:
            beam.apply_load(load.magnitude, load.start_location, -1)

        for moment in self.moments:
            beam.apply_load(moment.magnitude, moment.start_location, -2)

        for udl in self.udl:
            beam.apply_load(udl.magnitude,udl.start_location,0, end=udl.end_location)

    def apply_supports_to_sympy_beam_object(self, beam):
        for support in self.supports:
            beam.apply_support(support.location, support.supportType)

    def make_reaction_symbols_for_sympy_beam_object(self, beam):
        reaction_symbols = []
        for support in self.supports:
            if support.supportType == "fixed":
                reaction_symbols.extend(symbols('R_{0},M_{0}'.format(support.location)))
            else:
                reaction_symbols.append(symbols('R_{0}'.format(support.location)))
        return reaction_symbols



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

