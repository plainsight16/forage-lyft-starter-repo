from dataclasses import dataclass
from datetime import date
from battery.battery import Battery


@dataclass
class SpindlerBattery(Battery):
    last_service_date: date
    current_date: date

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 4)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False
