from abc import ABC, abstractmethod

from BEAM.Load.Moment import Moment
from BEAM.Load.PointLoad import PointLoad
from BEAM.Load.UDL import UDL


class Beam(ABC):

    def __init__(self, length):
        self.length = length
        self.cross_section = None
        self.material = None
        self.point_loads = []
        self.moments = []
        self.udl = []

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

