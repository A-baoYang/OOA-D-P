from channel_subscriber import ChannelSubscriber


class ComplicateUser(ChannelSubscriber):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def update(self, state: dict) -> dict:
        if "video" not in state:
            return state

        channel, video = state["channel"], state["video"]
        if video.length >= 300:
            self.like(video)
        elif video.length >= 180:
            self.dislike(video)
        elif video.length < 180:
            self.comment(video, message="可以拍長一點的影片嗎")

        if len(channel.video_list) == 3:
            self.unsubscribe(channel)

        return state
