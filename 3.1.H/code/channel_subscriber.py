from abc import ABC, abstractmethod
import arrow
import logging
import uuid


class ChannelSubscriber(ABC):
    def __init__(self, name: str) -> None:
        self._id = uuid.uuid4()
        self._name = name
        self._subscribed_channel_list = []
        self._liked_video_list = []

        logging.info(f"{self._name} 用戶加入了 Youtube")

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def subscribed_channel_list(self) -> list:
        return self._subscribed_channel_list

    @subscribed_channel_list.setter
    def subscribed_channel_list(self, subscribed_channel_list: list) -> None:
        self._subscribed_channel_list = subscribed_channel_list

    @property
    def liked_video_list(self) -> list:
        return self._liked_video_list

    @liked_video_list.setter
    def liked_video_list(self, liked_video_list: list) -> None:
        self._liked_video_list = liked_video_list

    def subscribe(self, channel: "Channel") -> None:
        self.subscribed_channel_list.append(channel)
        channel.add_subscriber(self)
        logging.info(f"{self.name} 訂閱了 {channel.name}")

    def unsubscribe(self, channel: "Channel") -> None:
        self.subscribed_channel_list.remove(channel)
        channel.remove_subscriber(self)
        logging.info(f"{self.name} 解除訂閱了 {channel.name}")

    def like(self, video: "Video") -> None:
        if video not in self.liked_video_list:
            self.liked_video_list.append(video)
        video.add_liker(self)
        logging.info(f'{self.name} 對影片 "{video.title}" 按讚。')

    def dislike(self, video: "Video") -> None:
        if video in self.liked_video_list:
            self.liked_video_list.remove(video)
        video.remove_liker(self)
        logging.info(f'{self.name} 對影片 "{video.title}" 按倒讚。')

    def comment(self, video: "Video", message: str) -> None:
        video.comments[self.id] = {
            "message": message,
            "datetime": arrow.now(tz="Asia/Taipei"),
        }
        logging.info(f'{self.name} 對影片 "{video.title}" 留言：「{message}」')

    @abstractmethod
    def behave(self, state: dict) -> dict:
        return state


class Waterball(ChannelSubscriber):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def behave(self, state: dict) -> dict:
        if "video" not in state:
            return state

        video = state["video"]
        if video.length >= 180:
            self.like(video)
        return state


class Fireball(ChannelSubscriber):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def behave(self, state: dict) -> dict:
        if "video" not in state:
            return state

        channel, video = state["channel"], state["video"]
        if video.length <= 60:
            self.unsubscribe(channel)
        return state
