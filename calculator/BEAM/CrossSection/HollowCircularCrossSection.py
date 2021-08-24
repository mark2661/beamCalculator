from BEAM.CrossSection.CrossSection import CrossSection
import math as maths

class HollowCircularCrossSection(CrossSection):

    def __init__(self,outer_radius, inner_radius, cross_section_type='Hollow Circular Cross-Section'):
        super(HollowCircularCrossSection, self).__init__(cross_section_type)
        self.outer_radius = outer_radius
        self.inner_radius = inner_radius

    #Override
    def get_area_moment_of_inertia(self):
        outer_diameter = 2 * self.outer_radius
        inner_diameter = 2 * self.inner_radius
        return (maths.pi * (pow(outer_diameter, 2) - pow(inner_diameter, 4))) / 64