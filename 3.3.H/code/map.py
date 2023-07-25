from dataclasses import dataclass
from typing import Union, List
import numpy as np
from pathlib import Path
import random

from CardGame.utils import read_data


@dataclass
class Map:
    height: int
    width: int

    def __post_init__(self) -> None:
        self.ROOT_DIR = Path(__name__).parent.absolute()
        self.matrix = np.zeros((self.height, self.width))
        self.space_num = self.height * self.width
        self.map_objects = read_data(str(self.ROOT_DIR / "config.yaml"))

    def _draw_position_on_map(self) -> np.array:
        pass

    def _get_current_left_space_num(self) -> int:
        """計算地圖剩下多少空間"""
        return self.space_num - len(self.map_objects)

    def _generate_random_position(self) -> List[int]:
        """隨機生成位置"""
        _position = None
        while _position is None or _position in self.map_objects.values():
            _position = [
                random.randint(0, self.height - 1),
                random.randint(0, self.width - 1),
            ]
        return _position

    def _generate_object_num(self) -> int:
        """隨機生成數量"""
        return random.randint(0, self._get_current_left_space_num() // 2 - 1)

    def initialize(self):
        """隨機生成三種 Map Object 的數量及位置
        - Obstcle
        - Treasure
        - Role(Monster)
        - Role(Chactrer)
        """
