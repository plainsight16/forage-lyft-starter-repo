from abc import ABC, abstractmethod


class Engine:
    @abstractmethod
    def needs_service(self) -> bool:
        pass
