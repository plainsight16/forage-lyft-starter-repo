from dataclasses import dataclass
from engine.engine import Engine
from battery.battery import Battery
from .serviceable import Serviceable


@dataclass
class Car(Serviceable):
    engine: Engine
    battery: Battery

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
