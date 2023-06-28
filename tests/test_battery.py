import unittest, sys
from datetime import datetime

sys.path.append('../forage-lyft-starter-repo-fork')

from models.Battery import NubbinBattery, SpindlerBattery

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
