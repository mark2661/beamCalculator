from Calculator.CrossSection.CrossSection import CrossSection


class RectangularCrossSection(CrossSection):

    def __init__(self, width, height, cross_section_type="Rectangle"):
        super(RectangularCrossSection, self).__init__(cross_section_type)
        self.width = width
        self.height = height

    #Override
    def get_area_moment_of_inertia(self):
        return (self.width * pow(self.height, 3)) / 12