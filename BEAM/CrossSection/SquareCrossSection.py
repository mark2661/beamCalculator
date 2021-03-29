from BEAM.CrossSection.RectangularCrossSection import RectangularCrossSection


class SquareCrossSection(RectangularCrossSection):
    
    def __init__(self, length):
        super(SquareCrossSection, self).__init__(length, length, "Square")