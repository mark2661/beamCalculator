from abc import ABC, abstractmethod

class CrossSection(ABC):

    def __init__(self, cross_section_type):
        self.cross_section_type = cross_section_type

    @abstractmethod
    def get_area_moment_of_inertia(self):
        pass