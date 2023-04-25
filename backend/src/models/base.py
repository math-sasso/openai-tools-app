from abc import ABC, abstractmethod


class BasePredictor(ABC):
    def __init__(self, **kwargs) -> None:
        pass

    @abstractmethod
    def predict(self, **kwargs) -> None:
        pass
