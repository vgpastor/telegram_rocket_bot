import unittest
from unittest.mock import Mock, patch
from src.application.RocketLaunchBot import RocketLaunchBot


class RocketLaunchBotTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Mock()
        self.video_service = Mock()
        self.video_service.get_video_info.return_value = Mock(frames=100)
        self.bot = RocketLaunchBot(self.app, self.video_service)

    def test_reset_data(self):
        # Configura el estado inicial de forma arbitraria
        self.bot.left_bound = 10
        self.bot.right_bound = 90

        # Llama a resetData y verifica si los límites se restablecen correctamente
        self.bot.resetData()
        self.assertEqual(self.bot.left_bound, 0)
        self.assertEqual(self.bot.right_bound, 99)

    @patch("src.application.RocketLaunchBot.Update")
    @patch("src.application.RocketLaunchBot.ContextTypes.DEFAULT_TYPE")
    async def test_start_bisection_search(self, mock_update, mock_context):
        await self.bot.start_bisection_search(mock_update, mock_context)
        self.assertEqual(self.bot.current_frame, 49)

    @patch("src.application.RocketLaunchBot.Update")
    @patch("src.application.RocketLaunchBot.ContextTypes.DEFAULT_TYPE")
    async def test_button_callback_yes(self, mock_update, mock_context):
        self.bot.current_frame = 49
        mock_update.callback_query = Mock(data='yes')

        await self.bot.button_callback(mock_update, mock_context)

        self.assertEqual(self.bot.right_bound, 49)
        self.assertEqual(self.bot.current_frame, 24)  # (0 + 49) // 2

    @patch("src.application.RocketLaunchBot.Update")
    @patch("src.application.RocketLaunchBot.ContextTypes.DEFAULT_TYPE")
    async def test_button_callback_no(self, mock_update, mock_context):
        self.bot.current_frame = 49
        mock_update.callback_query = Mock(data='no')

        await self.bot.button_callback(mock_update, mock_context)

        self.assertEqual(self.bot.left_bound, 50)
        self.assertEqual(self.bot.current_frame, 74)  # (50 + 99) // 2

    @patch("src.application.RocketLaunchBot.Update")
    @patch("src.application.RocketLaunchBot.ContextTypes.DEFAULT_TYPE")
    async def test_button_callback_done(self, mock_update, mock_context):
        self.bot.left_bound = 48
        self.bot.right_bound = 49
        self.bot.current_frame = 49
        mock_update.callback_query = Mock(data='yes', edit_message_text=AsyncMock())

        await self.bot.button_callback(mock_update, mock_context)

        mock_update.callback_query.edit_message_text.assert_called_with(text="¡El cohete despegó en el frame 49!")


if __name__ == "__main__":
    unittest.main()
