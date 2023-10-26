import unittest
from unittest.mock import Mock, patch
from src.application.RocketLaunchBot import RocketLaunchBot  # Asegúrate de importar la clase desde el módulo correcto
import asyncio


def async_test(f):
    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(f(*args, **kwargs))

    return wrapper


class TestRocketLaunchBot(unittest.TestCase):

    def setUp(self):
        self.mock_update = Mock(spec_set=["callback_query", "message"])
        self.mock_context = Mock()
        video_info_mock = Mock(frames=100)
        self.mock_video_service = Mock(get_video_info=Mock(return_value=video_info_mock),
                                       get_frame=Mock(return_value=Mock(url="http://example.com/frame.jpg")))
        self.bot = RocketLaunchBot(Mock(), self.mock_video_service)

    @async_test
    async def test_start_bisection_search(self):
        await self.bot.start_bisection_search(self.mock_update, self.mock_context)
        self.assertEqual(self.bot.current_frame, 49)  # Estamos comprobando si el frame inicial es el correcto

    @async_test
    async def test_button_callback_yes(self):
        self.bot.current_frame = 49
        self.mock_update.callback_query.data = 'yes'
        await self.bot.button_callback(self.mock_update, self.mock_context)
        self.assertEqual(self.bot.right_bound, 49)

    @async_test
    async def test_button_callback_no(self):
        self.bot.current_frame = 49
        self.mock_update.callback_query.data = 'no'
        await self.bot.button_callback(self.mock_update, self.mock_context)
        self.assertEqual(self.bot.left_bound, 50)


if __name__ == "__main__":
    unittest.main()
