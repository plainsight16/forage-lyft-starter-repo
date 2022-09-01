import unittest
from datetime import datetime
from ...engine.model.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(
            last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(
            last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
