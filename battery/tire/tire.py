from abc import ABC, abstractmethod


class Tire:
    @abstractmethod
    def needs_service(self):
        pass
