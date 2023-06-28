import unittest, sys
from datetime import datetime

sys.path.append('../forage-lyft-starter-repo-fork')

from models.Tires import CarriganTires, OctoprimeTires

class TestCarriganTires(unittest.TestCase):
    def test_should_be_serviced(self):
        tires = CarriganTires(tire_wear=[0.1, 0.2, 0.92, 0.93])
        self.assertTrue(tires.needs_service())

    def test_should_not_be_serviced(self):
        tires = CarriganTires(tire_wear=[0.5, 0.6, 0.03, 0.7])
        self.assertFalse(tires.needs_service())

class TestOctoprimeTires(unittest.TestCase):
    def test_should_be_serviced(self):
        tires = OctoprimeTires(tire_wear=[0.99, 0.99, 0.92, 0.93])
        self.assertTrue(tires.needs_service())

    def test_should_not_be_serviced(self):
        tires = OctoprimeTires(tire_wear=[0.1, 0.2, 0.92, 0.93])
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()