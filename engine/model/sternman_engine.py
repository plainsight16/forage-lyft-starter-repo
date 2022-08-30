from dataclasses import dataclass
from datetime import date
from engine.engine import Engine


@dataclass
class SternmanEngine(Engine):
    last_service_date: date
    warning_light_is_on: bool

    def engine_should_be_serviced(self) -> bool:
        if self.warning_light_is_on:
            return True
        else:
            return False
