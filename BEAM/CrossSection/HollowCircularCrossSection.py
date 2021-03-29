from BEAM.CrossSection.CrossSection import CrossSection


class HollowCircularCrossSection(CrossSection):

    def __init__(self,outer_radius, inner_radius, cross_section_type='Hollow Circular Cross-Section'):
        super(HollowCircularCrossSection, self).__init__(cross_section_type)
        self.outer_radius = outer_radius
        self.inner_radius = inner_radius

    #Override
    def get_area_moment_of_inertia(self):
        pass