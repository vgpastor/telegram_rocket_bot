from src.domain.model.VideoFrame import VideoFrame
from src.domain.model.VideoInfo import VideoInfo


class AbstractVideoService:
    def get_frame(self, id_video: str, frame_number: int) -> VideoFrame:
        raise NotImplementedError

    def get_video_info(self, id_video: str) -> VideoInfo:
        raise NotImplementedError

    def get_videos(self):
        raise NotImplementedError
