import unittest
from unittest.mock import patch, Mock
from src.domain.AbstractVideoService import AbstractVideoService
from src.domain.model.VideoInfo import VideoInfo
from src.domain.model.VideoFrame import VideoFrame
from src.infrastructure.framex.FrameXVideoService import FrameXVideoService

class FrameXVideoServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.service = FrameXVideoService()

    @patch("src.infrastructure.framex.FrameXVideoService.requests.get")
    def test_get_frame(self, mock_get):
        id_video = "test_video"
        frame_number = 123

        frame = self.service.get_frame(id_video, frame_number)

        self.assertEqual(frame.video_name, id_video)
        self.assertEqual(frame.frame, frame_number)
        self.assertEqual(frame.url, f"https://framex-dev.wadrid.net/api/video/{id_video}/frame/{frame_number}/")

    @patch("src.infrastructure.framex.FrameXVideoService.requests.get")
    def test_get_video_info(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            "name": "test_video",
            "frames": 500,
            "width": 1920,
            "height": 1080
        }
        mock_get.return_value = mock_response

        id_video = "test_video"
        video_info = self.service.get_video_info(id_video)

        self.assertEqual(video_info.name, "test_video")
        self.assertEqual(video_info.frames, 500)
        self.assertEqual(video_info.width, 1920)
        self.assertEqual(video_info.height, 1080)

    @patch("src.infrastructure.framex.FrameXVideoService.requests.get")
    def test_get_videos(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = [
            {
                "name": "test_video1",
                "frames": 500,
                "width": 1920,
                "height": 1080
            },
            {
                "name": "test_video2",
                "frames": 600,
                "width": 1280,
                "height": 720
            }
        ]
        mock_get.return_value = mock_response

        videos = self.service.get_videos()

        self.assertEqual(len(videos), 2)
        self.assertEqual(videos[0].name, "test_video1")
        self.assertEqual(videos[1].name, "test_video2")

if __name__ == "__main__":
    unittest.main()
