from BEAM.Material.Material import Material


class CastIronGrade20(Material):
    DENSITY = 7.15
    TENSILE_MODULUS = 100
    TENSILE_STRENGTH = 140

    def __init__(self):
        super(CastIronGrade20, self).__init__("Steel", CastIronGrade20.DENSITY, CastIronGrade20.TENSILE_MODULUS, CastIronGrade20.TENSILE_STRENGTH)