import unittest
from datetime import datetime
from ...engine.model.sternman_engine import SternmanEngine


class TestStrenmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        engine = SternmanEngine(
            last_service_date, warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        engine = SternmanEngine(
            last_service_date, warning_light_is_on)
        self.assertTrue(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
