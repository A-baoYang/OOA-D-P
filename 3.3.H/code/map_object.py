from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Union, List
import random


@dataclass
class MapObject(ABC):
    symbol: str
    name: str
    position: List[int]

    def __post_init__(self) -> None:
        pass
