from datetime import date
from car.car import Car
from engine.model.capulet_engine import CapuletEngine
from engine.model.willoughby_engine import WilloughbyEngine
from engine.model.sternman_engine import SternmanEngine
from battery.model.spindler import SpindlerBattery
from battery.model.nubbin import NubbinBattery


class CarFactory:
    def create_caliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        caliopeEngine = CapuletEngine(
            last_service_date, current_mileage, last_service_mileage)
        caliopeBattery = SpindlerBattery(last_service_date, current_date)
        return Car(caliopeEngine, caliopeBattery)

    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        glissadeEngine = WilloughbyEngine(
            last_service_date, current_mileage, last_service_mileage)
        glissadeBattery = SpindlerBattery(last_service_date, current_date)
        return Car(glissadeEngine, glissadeBattery)

    def create_palindrome(current_date: date, last_service_date: date, warning_light_is_on: bool):
        palindromeEngine = SternmanEngine(
            last_service_date, warning_light_is_on)
        palindromeBattery = SpindlerBattery(last_service_date, current_date)
        return Car(palindromeEngine, palindromeBattery)

    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        rorschachEngine = WilloughbyEngine(
            last_service_date, current_mileage, last_service_mileage)
        rorschachBattery = NubbinBattery(last_service_date, current_date)
        return Car(rorschachEngine, rorschachBattery)

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        thovexEngine = CapuletEngine(
            last_service_date, current_mileage, last_service_mileage)
        thovexBattery = NubbinBattery(last_service_date, current_date)
        return Car(thovexEngine, thovexBattery)
