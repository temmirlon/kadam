from abc import ABC, abstractmethod

class ActivityProvider(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass