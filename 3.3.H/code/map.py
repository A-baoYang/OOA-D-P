from dataclasses import dataclass
import numpy as np


@dataclass
class Map:
    height: int
    width: int

    def __post_init__(self) -> None:
        self.matrix = np.zeros((self.height, self.width))
