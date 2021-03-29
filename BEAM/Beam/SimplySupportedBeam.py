from abc import ABC

from BEAM.Beam.Beam import Beam


class SimplySupportedBeam(Beam, ABC):

    def __init__(self, length, cross_section, material):
        super.__init__(length, cross_section, material)

