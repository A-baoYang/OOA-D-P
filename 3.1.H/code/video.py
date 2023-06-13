import logging
from typing import Any
import uuid


class Video:
    def __init__(self, title: str, description: str, length: int) -> None:
        self._id = uuid.uuid4()
        self._title = title
        self._description = description
        self._length = length
        self._liked_users = []
        self._disliked_users = []
        self._comments = {}

        logging.info(f"{self._title} 影片建立")

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        self._title = title

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        self._description = description

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, length: int) -> None:
        self._length = length

    @property
    def liked_users(self) -> list:
        return self._liked_users

    @liked_users.setter
    def liked_users(self, liked_users: list) -> None:
        self._liked_users = liked_users

    @property
    def disliked_users(self) -> list:
        return self._disliked_users

    @disliked_users.setter
    def disliked_users(self, disliked_users: list) -> None:
        self._disliked_users = disliked_users

    @property
    def comments(self) -> dict:
        return self._comments

    @comments.setter
    def comments(self, comments: dict) -> None:
        self._comments = comments

    def add_liker(self, user: Any) -> None:
        if user not in self.liked_users:
            self.liked_users.append(user)
        if user in self.disliked_users:
            self.disliked_users.remove(user)

    def remove_liker(self, user: Any) -> None:
        if user not in self.disliked_users:
            self.disliked_users.append(user)
        if user in self.liked_users:
            self.liked_users.remove(user)
