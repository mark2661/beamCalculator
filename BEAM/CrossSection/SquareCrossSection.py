from BEAM.CrossSection.RectangularCrossSection import RectangularCrossSection


class SquareCrossSection(RectangularCrossSection):
    
    def __init__(self, length):
        super(SquareCrossSection, self).__init__(length, length, "Square")

    # Override
    def get_area_moment_of_inertia(self):
        return pow(self.height, 4) / 12
