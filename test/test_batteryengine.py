import unittest
from battery.battery import Battery
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from utils import add_years_to_date
from engine.engine import Engine

class BatteryTest(unittest.TestCase):
    def test_needs_service_abstract_method(self):
        battery = Battery()
        with self.assertRaises(NotImplementedError):
            battery.needs_service()


class NubbinBatteryTest(unittest.TestCase):
    def test_needs_service_returns_true_when_last_service_date_is_more_than_4_years_ago(self):
        current_date = datetime.datetime(2023, 11, 7)
        last_service_date = datetime.datetime(2019, 11, 7)
        battery = NubbinBattery(current_date, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_needs_service_returns_false_when_last_service_date_is_less_than_4_years_ago(self):
        current_date = datetime.datetime(2023, 11, 7)
        last_service_date = datetime.datetime(2021, 11, 7)
        battery = NubbinBattery(current_date, last_service_date)

        self.assertFalse(battery.needs_service())

class SpindlerBatteryTest(unittest.TestCase):
    def test_needs_service_returns_true_when_last_service_date_is_more_than_2_years_ago(self):
        current_date = datetime.datetime(2023, 11, 7)
        last_service_date = datetime.datetime(2021, 11, 7)
        battery = SpindlerBattery(current_date, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_needs_service_returns_false_when_last_service_date_is_less_than_2_years_ago(self):
        current_date = datetime.datetime(2023, 11, 7)
        last_service_date = datetime.datetime(2023, 5, 7)
        battery = SpindlerBattery(current_date, last_service_date)

        self.assertFalse(battery.needs_service())

class EngineTest(unittest.TestCase):
    def test_needs_service_abstract_method(self):
        engine = Engine()
        with self.assertRaises(NotImplementedError):
            engine.needs_service()
