import unittest, sys
from datetime import datetime

sys.path.append('../forage-lyft-starter-repo-fork')

from models.Engine import CapuletEngine, WilloughbyEngine, SternmanEngine


class TestCapuletEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        engine = CapuletEngine(last_service_mileage=30001, current_mileage=0)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        engine = CapuletEngine(last_service_mileage=3001, current_mileage=0)
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_should_be_serviced(self):

        engine = WilloughbyEngine(last_service_mileage=60001, current_mileage=0)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        engine = WilloughbyEngine(last_service_mileage=5999, current_mileage=0)
        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        warning_light = True
        engine = SternmanEngine(warning_light)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        warning_light = False
        engine = SternmanEngine(warning_light)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
