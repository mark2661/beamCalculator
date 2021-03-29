from abc import ABC

from BEAM.Load.PointLoad import PointLoad


class Support(ABC):

    def __init__(self, location, vertical_reaction=None, type=None):
        self.location = location
        self.vertical_reaction = vertical_reaction
        self.type = type

    def set_vertical_reaction(self, magnitude):
        new_vertical_reaction = PointLoad(magnitude,self.location)
        self.vertical_reaction = new_vertical_reaction