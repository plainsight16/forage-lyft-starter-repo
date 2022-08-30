from abc import ABC, abstractmethod
from dataclasses import dataclass
from engine.engine import Engine
from battery.battery import Battery


@dataclass
class Car(ABC):
    engine: Engine
    battery: Battery

    def needs_service(self):
        if self.battery.needs_service() or self.engine.needs_service():
            return True
        else:
            return False
