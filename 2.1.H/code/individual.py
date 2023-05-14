"""定義用戶資訊"""
from typing import Any, List

from coordinate import Coord


class Individual:
    """類別：用戶"""

    def __init__(
        self,
        uid: int,
        gender: str,
        age: int,
        intro: str,
        habits: List[str],
        coord: Coord,
    ) -> None:

        assert isinstance(uid, int) and uid > 0, TypeError("id 須為正整數")
        self._uid = uid
        print(f"User#{self._uid} registered successfully")
        assert gender in ["MALE", "FEMALE"], TypeError("gender 需為 MALE 或 FEMALE")
        self._gender = gender
        assert age >= 18, TypeError("交友系統僅對 18 以上用戶開放")
        self._age = age
        assert len(intro) <= 200, TypeError("自我介紹須在 200 字以內")
        self._intro = intro
        assert len(habits) <= 10, TypeError("興趣關鍵字上限為 10 個")
        self._habits = habits
        assert isinstance(coord, Coord), TypeError("座標應從 Coord 類別實作")
        self._coord = coord

    def __repr__(self) -> str:
        return f"Individual#{self._uid}"

    def __getattr__(self, __name: str):
        return self.__dict__[f"__{__name}"]

    def __setattr__(self, __name: str, __value: Any) -> None:
        self.__dict__[f"__{__name}"] = __value

    @property
    def uid(self):
        """取得用戶 ID"""
        return self._uid

    @property
    def gender(self):
        """取得用戶性別"""
        return self._gender

    @property
    def age(self):
        """取得用戶年齡"""
        return self._age

    @property
    def intro(self):
        """取得用戶自介"""
        return self._intro

    @property
    def habits(self):
        """取得用戶興趣列表"""
        return self._habits

    @property
    def coord(self):
        """取得用戶坐標"""
        return self._coord

    @uid.setter
    def uid(self, uid: int):
        assert isinstance(uid, int) and uid > 0, TypeError("id 須為正整數")
        self._uid = uid

    @gender.setter
    def gender(self, gender: str):
        assert gender in ["MALE", "FEMALE"], TypeError("gender 需為 MALE 或 FEMALE")
        self._gender = gender

    @age.setter
    def age(self, age: int):
        assert age >= 18, TypeError("交友系統僅對 18 以上用戶開放")
        self._age = age

    @intro.setter
    def intro(self, intro: str):
        assert len(intro) <= 200, TypeError("自我介紹須在 200 字以內")
        self._intro = intro

    @habits.setter
    def habits(self, habits: List[str]):
        assert len(habits) <= 10, TypeError("興趣關鍵字上限為 10 個")
        self._habits = habits

    @coord.setter
    def coord(self, coord: Coord):
        assert isinstance(coord, Coord), TypeError("座標應從 Coord 類別實作")
        self._coord = coord
