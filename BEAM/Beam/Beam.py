from abc import ABC, abstractmethod

from BEAM.Load.Moment import Moment
from BEAM.Load.PointLoad import PointLoad
from BEAM.Load.UDL import UDL
from sympy.physics.continuum_mechanics.beam import Beam as sympyBeam
from sympy import *



class Beam(ABC):

    def __init__(self, length,cross_section, material):
        self.length = length
        self.cross_section = cross_section
        self.material = material
        self.point_loads = []
        self.moments = []
        self.udl = []
        self.supports = []

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

    def calculate(self):
        E = self.material.tensile_modulus
        I = self.cross_section.get_moment_of_inertia()

        beam = sympyBeam(self.length, E, I)
        self.apply_loads(beam)
        self.apply_supports(beam)
        beam.solve_for_reaction_loads()

    def apply_loads(self,beam):
        for load in self.point_loads:
            beam.apply_load(load.magnitude, load.start_location, -1)

        for moment in self.moments:
            beam.apply_load(moment.magnitude, moment.start_location, -2)

    def apply_supports(self, beam):
        for support in self.supports:
            beam.apply_support(support.location, support.type)


    """
    ** ABSTRACT METHODS **
    """
    @abstractmethod
    def calculate_max_moment(self):
        pass

    @abstractmethod
    def calculate_moment_at_location_x(self,x):
        pass

    @abstractmethod
    def calculate_max_deflection(self):
        pass

    @abstractmethod
    def calculate_deflection_at_location_x(self,x):
        pass

    @abstractmethod
    def calculate_max_shear_force(self):
        pass

    @abstractmethod
    def calculate_shear_force_at_location_x(self,x):
        pass

    @abstractmethod
    def calculate_support_reactions(self):
        pass

