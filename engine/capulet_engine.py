from dataclasses import dataclass
from datetime import date
from engine import Engine


@dataclass
class CapuletEngine(Engine):
    last_service_date: date
    current_mileage: int
    last_service_mileage: int

    def engine_should_be_serviced(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 30000
