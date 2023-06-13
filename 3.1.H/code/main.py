from channel import Channel
from channel_subscriber import Waterball, Fireball
from ocp_new_type_subscriber import ComplicateUser
from video import Video
from CardGame.utils import log_setting, read_data


def main():
    sample_data = read_data(path="../data/example.json")

    channels = {}
    for channel in sample_data["channels"]:
        channels[channel["name"]] = Channel(name=channel["name"])

    subscribers = {}
    for user in sample_data["subscribers"]:
        channel_type_cls = {"水球": Waterball, "火球": Fireball, "難懂的用戶": ComplicateUser}
        subscribers[user["name"]] = channel_type_cls[user["name"]](name=user["name"])

    videos = {}
    for video in sample_data["videos"]:
        videos[video["title"]] = Video(
            title=video["title"],
            description=video["description"],
            length=video["length"],
        )

    for channel in channels.values():
        for subscriber in subscribers.values():
            subscriber.subscribe(channel)

    channels["水球軟體學院"].upload(video=videos["C1M1S2"])
    channels["PewDiePie"].upload(video=videos["Hello guys"])
    channels["水球軟體學院"].upload(video=videos["C1M1S3"])
    channels["PewDiePie"].upload(video=videos["Minecraft"])
    channels["PewDiePie"].upload(video=videos["Minecraft PartII"])


if __name__ == "__main__":
    log_setting()
    main()
