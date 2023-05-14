"""定義生物資訊"""
from typing import Any


class Sprite:
    """類別：生物"""

    def __init__(self, coord: int) -> None:
        assert isinstance(coord, int) and coord >= 0 and coord < 30, TypeError(
            "coord 須為 0 ~ 29 正整數"
        )
        self._coord = coord

    def __repr__(self) -> str:
        return f"{type(self)} (x: {self._coord})"

    @property
    def coord(self):
        """取得生物座標"""
        return self._coord

    @coord.setter
    def coord(self, coord: int):
        assert isinstance(coord, int) and coord >= 0 and coord < 30, TypeError(
            "coord 須為 0 ~ 29 正整數"
        )
        self._coord = coord


class Hero(Sprite):
    def __init__(self, coord: int) -> None:
        super().__init__(coord)

        self._HP = 30

    @property
    def HP(self):
        return self._HP

    @HP.setter
    def HP(self, hp: int):
        if hp < 0:
            hp = 0
        elif hp > 30:
            hp = 30
        assert isinstance(hp, int)
        self._HP = hp


class Water(Sprite):
    def __init__(self, coord: int) -> None:
        super().__init__(coord)


class Fire(Sprite):
    def __init__(self, coord: int) -> None:
        super().__init__(coord)
