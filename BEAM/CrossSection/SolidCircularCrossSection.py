from BEAM.CrossSection.HollowCircularCrossSection import HollowCircularCrossSection
import math as maths


class SolidCircularCrossSection(HollowCircularCrossSection):

    def __init__(self,radius):
        super(SolidCircularCrossSection, self).__init__(radius, 0, "Solid Circular Cross-Section")

    def get_area_moment_of_inertia(self):
        return (maths.pi * pow(self.outer_radius,4)) / 4
