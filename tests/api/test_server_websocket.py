from __future__ import annotations

import unittest

from atguigu_ai.api.server import AtguiguServer


class ClosedWebSocket:
    def __init__(self) -> None:
        self.send_count = 0

    async def send_json(self, message: object) -> None:
        self.send_count += 1
        raise RuntimeError(
            "Unexpected ASGI message 'websocket.send', after sending 'websocket.close'."
        )


class WebSocketSendTest(unittest.IsolatedAsyncioTestCase):
    async def test_safe_websocket_send_reports_closed_connection(self) -> None:
        websocket = ClosedWebSocket()

        sent = await AtguiguServer._safe_websocket_send(
            websocket,
            {"type": "bot_response", "data": []},
        )

        self.assertFalse(sent)
        self.assertEqual(websocket.send_count, 1)
