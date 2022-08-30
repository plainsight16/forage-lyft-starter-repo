from abc import ABC, abstractmethod
from dataclasses import dataclass
from engine.engine import Engine
from battery.battery import Battery


@dataclass
class Car(ABC):
    engine: Engine
    battery: Battery

    @abstractmethod
    def needs_service(self):
        pass
