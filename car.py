from dataclasses import dataclass
from engine.engine import Engine
from battery.battery import Battery
from tire.tire import Tire
from .serviceable import Serviceable


@dataclass
class Car(Serviceable):
    engine: Engine
    battery: Battery
    tire: Tire

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service() or self.tire.needs_service()
