from datetime import date
from car import Car
from engine.model.capulet_engine import CapuletEngine
from engine.model.willoughby_engine import WilloughbyEngine
from engine.model.sternman_engine import SternmanEngine
from battery.model.spindler import SpindlerBattery
from battery.model.nubbin import NubbinBattery
from tire.model.carrigan import Carrigan
from tire.model.octoprime import Octoprime


class CarFactory:

    @staticmethod
    def create_caliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tear_wear: list):
        caliopeEngine = CapuletEngine(
            last_service_date, current_mileage, last_service_mileage)
        caliopeBattery = SpindlerBattery(last_service_date, current_date)
        caliopeTire = Carrigan(tear_wear)
        return Car(caliopeEngine, caliopeBattery, caliopeTire)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tear_wear: list):
        glissadeEngine = WilloughbyEngine(
            last_service_date, current_mileage, last_service_mileage)
        glissadeBattery = SpindlerBattery(last_service_date, current_date)
        glissadeTire = Carrigan(tear_wear)
        return Car(glissadeEngine, glissadeBattery, glissadeTire)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_is_on: bool, tear_wear: list):
        palindromeEngine = SternmanEngine(
            last_service_date, warning_light_is_on)
        palindromeBattery = SpindlerBattery(last_service_date, current_date)
        palidromeTire = Octoprime(tear_wear)
        return Car(palindromeEngine, palindromeBattery, palidromeTire)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tear_wear: list):
        rorschachEngine = WilloughbyEngine(
            last_service_date, current_mileage, last_service_mileage)
        rorschachBattery = NubbinBattery(last_service_date, current_date)
        rorschachTire = Octoprime(tear_wear)
        return Car(rorschachEngine, rorschachBattery, rorschachTire)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tear_wear: list):
        thovexEngine = CapuletEngine(
            last_service_date, current_mileage, last_service_mileage)
        thovexBattery = NubbinBattery(last_service_date, current_date)
        thovexTire = Carrigan(tear_wear)
        return Car(thovexEngine, thovexBattery, thovexTire)
