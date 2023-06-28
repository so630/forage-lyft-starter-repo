import unittest
from datetime import datetime

from models.Engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from models.Battery import NubbinBattery, SpindlerBattery

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

    def test_should_be_serviced(self):
        warning_light = False
        engine = SternmanEngine(warning_light)
        self.assertFalse(engine.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        current_date = datetime.now()
        last_service_date = current_date.replace(year=(current_date.year - 3))

        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self):
        current_date = datetime.now()
        last_service_date = current_date.replace(year=(current_date.year - 1))

        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        self.assertFalse(battery.needs_service())

class TestNubbinBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        current_date = datetime.now()
        last_service_date = current_date.replace(year=(current_date.year - 5))

        battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self):
        current_date = datetime.now()
        last_service_date = current_date.replace(year=(current_date.year - 2))

        battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
