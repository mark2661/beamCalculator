from BEAM.CrossSection.HollowCircularCrossSection import HollowCircularCrossSection


class SolidCircularCrossSection(HollowCircularCrossSection):

    def __init__(self,radius):
        super(SolidCircularCrossSection, self).__init__(radius, 0, "Solid Circular Cross-Section")
