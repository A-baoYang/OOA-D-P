"""定義座標及距離計算方式"""
import math


class Coord:
    """類別：座標"""

    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    @property
    def x(self):
        """取得 x 座標"""
        return self._x

    @x.setter
    def x(self, new_x: float):
        self._x = new_x

    @property
    def y(self):
        """取得 y 座標"""
        return self._y

    @y.setter
    def y(self, new_y: float):
        self._y = new_y

    def __sub__(self, target_coord: "Coord") -> float:
        """計算兩座標間距離"""
        return math.sqrt(
            sum(
                [
                    (i - j) ** 2
                    for i, j in zip(
                        [self._x, self._y], [target_coord.x, target_coord.y]
                    )
                ]
            )
        )
