import unittest
from datetime import datetime
from ...engine.model.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(
            last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(
            last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
