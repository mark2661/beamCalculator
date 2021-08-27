from beamCalculator.Calculator.Load.Load import Load


class Moment(Load):

    def __init__(self, magnitude, start_location):
        super(Moment, self).__init__(magnitude, start_location, start_location)  # For moment start location = end location