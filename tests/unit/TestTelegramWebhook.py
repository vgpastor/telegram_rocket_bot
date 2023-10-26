import unittest
import json
from aiohttp import web
from aiohttp.test_utils import TestServer, TestClient, unittest_run_loop
from test import TelegramBotServer  # Asume que la clase anterior está en el archivo test.py

class TestTelegramBotServer(unittest.TestCase):
    async def setUpAsync(self):
        self.server = TelegramBotServer()
        await self.server.init_app()
        self.test_server = TestServer(self.server.app)
        self.client = TestClient(self.test_server)
        await self.client.start_server()

    async def tearDownAsync(self):
        await self.client.close()

    @unittest_run_loop
    async def test_handle(self):
        data = {
            "message": {
                "chat": {"id": 12345},
                "text": "Hola"
            }
        }
        response = await self.client.post('/telegram_webhook', json=data)
        self.assertEqual(response.status, 200)
        content = await response.text()
        self.assertEqual(content, "")  # Esperamos una respuesta vacía

    # Puedes agregar más tests según las funcionalidades de tu bot

if __name__ == "__main__":
    unittest.main()

