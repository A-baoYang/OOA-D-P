"""定義世界資訊"""
from typing import Union, Any
from collections import defaultdict
import numpy as np
import random

from sprite import Sprite, Hero, Water, Fire
from collisionHandleChain import CollisionHandleChain


class World:
    """類別：世界"""

    def __init__(self) -> None:
        self._length = 30
        self._sprites = defaultdict(lambda: None)
        self.collisionHandleChain = CollisionHandleChain()
        self.collisionHandleChain.chain()

    def __repr__(self) -> str:
        return f"World ({self._length})"

    def __getattr__(self, __name: str):
        return self.__dict__[f"__{__name}"]

    def __setattr__(self, __name: str, __value: Any) -> None:
        self.__dict__[f"__{__name}"] = __value

    @property
    def length(self):
        """取得世界長度"""
        return self._length

    @property
    def sprites(self):
        """取得世界所有生物及其座標"""
        return self._sprites

    def init(self, mode: str) -> None:
        if mode == "random":
            _positions = list(
                set(
                    np.random.randint(
                        low=0,
                        high=self._length - 1,
                        size=random.randint(1, self._length - 1),
                    ).tolist()
                )
            )
            for i in _positions:
                sprite_type = random.choice([Hero, Water, Fire])
                c = sprite_type(coord=i)
                self.add_sprite(coord=i, sprite=c)
        else:
            raise Warning("this mode hasn't been set before")

    def get_sprite(self, coord: int) -> Union[Sprite, None]:
        """從座標取得生物"""
        return self._sprites[coord]

    def add_sprite(self, coord: int, sprite: Sprite) -> None:
        """在指定坐標上放置生物"""
        assert isinstance(coord, int) and coord >= 0 and coord < 30, TypeError(
            "coord 須為 0 ~ 29 正整數"
        )
        if not self._sprites[coord]:
            self._sprites[coord] = sprite
        else:
            raise Exception(f"{coord} already has a sprite: {sprite}")

    def move_sprite(self, source_coord: int, target_coord: int):
        if not self._sprites[target_coord]:
            self._sprites[target_coord] = self._sprites[source_coord]
            del self._sprites[source_coord]
        else:
            raise Exception(
                f"target_coord still has sprite: {self._sprites[target_coord]} ({target_coord})"
            )

    def remove_sprite(self, coord: int) -> None:
        del self._sprites[coord]
