from src.domain.AbstractVideoService import AbstractVideoService
from src.domain.model.VideoInfo import VideoInfo
from src.domain.model.VideoFrame import VideoFrame
import requests
class FrameXVideoService(AbstractVideoService):
    API_BASE_URL = "https://framex-dev.wadrid.net/api/video/"

    def get_frame(self, id_video: str, frame_number: int) -> VideoFrame:
        return VideoFrame(id_video,frame_number,f"{self.API_BASE_URL}{id_video}/frame/{frame_number}/")

    def get_video_info(self, id_video: str) -> VideoInfo:
        response = requests.get(f"{self.API_BASE_URL}{id_video}/")
        data = response.json()
        return VideoInfo(data["name"], data["frames"], data["width"], data["height"])

    def get_videos(self):
        response = requests.get(self.API_BASE_URL)
        data_list = response.json()
        return [VideoInfo(data["name"], data["frames"], data["width"], data["height"]) for data in data_list]
