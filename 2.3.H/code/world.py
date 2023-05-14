"""定義世界資訊"""
from typing import Union
from collections import defaultdict
import random

from sprite import Sprite, Hero, Water, Fire
from collisionHandleChain import CollisionHandleChain


class World:
    """類別：世界"""

    def __init__(self) -> None:
        self._length = 30
        self._sprites = list()
        self._sprites_position_dict = defaultdict(lambda: None)
        self._collisionHandleChain = CollisionHandleChain()
        self._collisionHandleChain.chain()

    def __repr__(self) -> str:
        return f"World ({self._length})"

    @property
    def length(self):
        """取得世界長度"""
        return self._length

    @property
    def sprites(self):
        """取得世界所有生物"""
        return self._sprites

    @property
    def sprites_position_dict(self):
        """取得世界所有生物及其座標"""
        return self._sprites_position_dict

    def init(self, mode: str) -> None:
        if mode == "random":
            _positions = random.sample(
                range(self._length - 1), random.randint(1, self._length - 1)
            )
            for i in _positions:
                sprite_type = random.choice([Hero, Water, Fire])
                self.add_sprite(sprite=sprite_type(coord=i))
        else:
            raise Warning("this mode hasn't been set before")

        self.arrange_sprites()

    def get_sprite(self, coord: int) -> Union[Sprite, None]:
        """從座標取得生物"""
        return self._sprites_position_dict[coord]

    def arrange_sprites(self) -> None:
        """將串列中的生物位置轉成索引字典"""
        self._sprites_position_dict = defaultdict(
            lambda: None,
            sorted({item.coord: item for item in self._sprites}.items(), reverse=False),
        )

    def add_sprite(self, sprite: Sprite) -> None:
        """加入生物到串列"""
        self._sprites.append(sprite)
        # """在指定坐標上放置生物"""
        # position = sprite.coord
        # if not self._sprites_position_dict[position]:
        #     self._sprites_position_dict[position] = sprite
        # else:
        #     raise Exception(f"The position: {position} already has a sprite: {sprite}")

    def move_sprite(self, source_coord: int, target_coord: int):
        """將生物移動到指定坐標上"""
        source_sprite, target_sprite = (
            self._sprites_position_dict[source_coord],
            self._sprites_position_dict[target_coord],
        )
        if not target_sprite:
            source_sprite.coord = target_coord
            self._sprites_position_dict[target_coord] = source_sprite
            self._sprites_position_dict[source_coord] = None
        else:
            raise Exception(
                f"target_coord still has sprite: {target_sprite} ({target_coord})"
            )

    def remove_sprite(self, coord: int) -> None:
        del self._sprites_position_dict[coord]
