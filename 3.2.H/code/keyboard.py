from typing import List


class Key:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self.name = name


class Keyboard:
    def __init__(self, keys: List[Key]) -> None:
        self._keys = keys

    @property
    def keys(self) -> list:
        return self._keys

    @keys.setter
    def keys(self, keys: List[Key]) -> None:
        self._keys = keys
