from typing import Union, List
from map_object import MapObject


class Role(MapObject):
    def __init__(self, symbol: Union[str, dict], name: str) -> None:
        self._symbol = symbol
        self._name = name

    def _get_random_position(self, map: "Map"):
        return [random.randint(0, map.height - 1), random.randint(0, map.width - 1)]
