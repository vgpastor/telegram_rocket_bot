from src.domain.model.VideoInfo import VideoInfo

class VideoFrame:
    def __init__(self, video_name: str, frame: int, url: str):
        self.video_name = video_name
        self.frame = frame
        self.url = url

    def __str__(self):
        return f"VideoFrame(video_name={self.video_name}, frame={self.frame}, url={self.url})"

    def __repr__(self):
        return self.__str__()
