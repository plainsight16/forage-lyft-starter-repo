from array import array
from dataclasses import dataclass
from tire.tire import Tire


@dataclass
class Carrigan(Tire):
    wear_condition: list

    def needs_service(self):
        for condition in self.wear_condition:
            if condition > 0.9:
                return True

        return False
