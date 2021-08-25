from Calculator.Load.Load import Load


class UDL(Load):

    def __init__(self, magnitude, start_location, end_location):
        super(UDL, self).__init__(magnitude, start_location, end_location)