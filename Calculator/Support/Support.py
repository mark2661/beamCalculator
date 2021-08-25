from abc import ABC

from Calculator.Load.PointLoad import PointLoad


class Support(ABC):

    def __init__(self, location, supportType=None, vertical_reaction=None):
        self.location = location
        self.vertical_reaction = vertical_reaction
        self.supportType = supportType

    def set_vertical_reaction(self, magnitude):
        new_vertical_reaction = PointLoad(magnitude,self.location)
        self.vertical_reaction = new_vertical_reaction