import sys
import uuid

sys.path.append("../code")
from channel import Channel
from channel_subscriber import Waterball
from video import Video


def test_channel():
    channel = Channel(name="Hi")
    assert isinstance(channel.id, uuid.UUID)
    assert isinstance(channel.name, str)


def test_video():
    video = Video(title="test title", description="test test test", length=300)
    assert isinstance(video.id, uuid.UUID)
    assert isinstance(video.title, str)
    assert isinstance(video.description, str)
    assert isinstance(video.length, int) and video.length > 0


def test_subscriber():
    subscriber = Waterball(name="test waterball")
    assert isinstance(subscriber.id, uuid.UUID)
    assert isinstance(subscriber.name, str)

