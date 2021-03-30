import unittest
from BEAM import *
from BEAM.Beam.SimplySupportedBeam import SimplySupportedBeam
from BEAM.CrossSection.SquareCrossSection import SquareCrossSection
from BEAM.Material.SteelAISI1045 import SteelAISI1045


class MyTestCase(unittest.TestCase):


    def test_simplySupportedBeamObjectCreation(self):
        test_beam = SimplySupportedBeam(1, SquareCrossSection(0.1), SteelAISI1045())
        self.assertEqual(test_beam.length, 1)

        #CHECK CROSS-SECTION PROPERTIES
        self.assertEqual(test_beam.cross_section.cross_section_type, "Square")

        #CHECK MATERIAL PROPERTIES
        self.assertEqual(test_beam.material.material_type, "Steel")
        self.assertEqual(test_beam.material.DENSITY, 8)
        self.assertEqual(test_beam.material.TENSILE_MODULUS, 205)
        self.assertEqual(test_beam.material.TENSILE_STRENGTH, 585)


    def test_add_point_load(self):
        test_beam = SimplySupportedBeam(1, SquareCrossSection(0.1), SteelAISI1045())
        self.assertTrue(len(test_beam.point_loads) == 0)

        #CHECK POINTLOAD OBJECT ADDED TO POINTLOAD LIST
        test_beam.add_point_load(100, 0.5)
        self.assertTrue(len(test_beam.point_loads) == 1)

        #Check force object properties
        self.assertEqual(test_beam.point_loads[0].magnitude, 100)
        self.assertEqual(test_beam.point_loads[0].start_location, 0.5)

        #CHECK CLEAR LOADS FUNCTION
        test_beam.clear_loads()
        self.assertTrue(len(test_beam.point_loads) == 0)

    def test_add_support(self):
        test_beam = SimplySupportedBeam(1, SquareCrossSection(0.1), SteelAISI1045())
        self.assertTrue(len(test_beam.supports) == 0)

        #CHECK PIN SUPPORT
        test_beam.add_pin_support(0)
        self.assertTrue(len(test_beam.supports) == 1)
        self.assertEqual(test_beam.supports[0].supportType, "pin")
        self.assertEqual(test_beam.supports[0].location, 0)

        #CHECK ROLLER SUPPORTS
        test_beam.add_roller_support(1)
        self.assertTrue(len(test_beam.supports) == 2)
        self.assertEqual(test_beam.supports[1].supportType, "roller")
        self.assertEqual(test_beam.supports[1].location, 1)

        #CHECK CLEAR SUPPORTS
        test_beam.clear_supports()
        self.assertTrue(len(test_beam.supports) == 0)




if __name__ == '__main__':
    unittest.main()
