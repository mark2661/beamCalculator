from abc import ABC, abstractmethod

class Material(ABC):

    def __init__(self, material_type, density, tensile_modulus, tensile_strength):
        self.material_type = material_type
        self.density = density
        self.tensile_modulus = tensile_modulus
        self.tensile_strength = tensile_strength



