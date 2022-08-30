from dataclasses import dataclass
from datetime import date
from battery.battery import Battery


@dataclass
class NubbinBattery(Battery):
    last_service_date: date
    current_date: date

    def needs_service(self) -> bool:
        pass
