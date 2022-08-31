from dataclasses import dataclass
from tire.tire import Tire


@dataclass
class Octoprime(Tire):
    tire_wear: list

    def needs_service(self):
        sum = 0
        for condition in self.wear_condition:
            sum += condition
            if sum >= 3:
                return True

        return False
