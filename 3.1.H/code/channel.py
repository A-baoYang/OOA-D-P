import logging
import uuid

from channel_subscriber import ChannelSubscriber
from video import Video


class Channel:
    def __init__(self, name: str) -> None:
        self._id = uuid.uuid4()
        self._name = name
        self._subscriber_list = []
        self._video_list = []

        logging.info(f"Youtube 頻道 {self.name} 創立")

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
    def video_list(self) -> list:
        return self._video_list

    @video_list.setter
    def video_list(self, video_list: list) -> None:
        self._video_list = video_list

    @property
    def subscriber_list(self) -> list:
        return self._subscriber_list

    @subscriber_list.setter
    def subscriber_list(self, subscriber_list: list) -> None:
        self._subscriber_list = subscriber_list

    def upload(self, video: Video) -> None:
        self.video_list.append(video)
        logging.info(f"頻道 {self.name} 上架了一則新影片 {video.title}")
        self.notify(state={"video": video, "channel": self})

    def add_subscriber(self, subscriber: ChannelSubscriber) -> None:
        self.subscriber_list.append(subscriber)

    def remove_subscriber(self, subscriber: ChannelSubscriber) -> None:
        self.subscriber_list.remove(subscriber)

    def notify(self, state: dict) -> None:
        subscribers_to_notify = self.subscriber_list.copy()
        for subscriber in subscribers_to_notify:
            subscriber.behave(state)
