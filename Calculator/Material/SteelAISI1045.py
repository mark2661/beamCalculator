from Calculator.Material.Material import Material


class SteelAISI1045(Material):
    DENSITY = 8
    TENSILE_MODULUS = 205
    TENSILE_STRENGTH = 585
    
    def __init__(self):
        super(SteelAISI1045, self).__init__("Steel", SteelAISI1045.DENSITY, SteelAISI1045.TENSILE_MODULUS, SteelAISI1045.TENSILE_STRENGTH)