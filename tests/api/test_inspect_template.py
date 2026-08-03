from pathlib import Path
import unittest


class InspectTemplateTest(unittest.TestCase):
    def test_inspect_page_displays_websocket_error_messages(self) -> None:
        template = (
            Path(__file__).parents[2]
            / "atguigu_ai"
            / "api"
            / "templates"
            / "inspect.html"
        ).read_text(encoding="utf-8")

        self.assertIn("data.type === 'error'", template)
        self.assertIn("addMessage(data.message", template)

    def test_inspect_page_reuses_session_id_after_refresh(self) -> None:
        template = (
            Path(__file__).parents[2]
            / "atguigu_ai"
            / "api"
            / "templates"
            / "inspect.html"
        ).read_text(encoding="utf-8")

        self.assertIn("localStorage.getItem('atguigu-inspect-session-id')", template)
        self.assertIn("localStorage.setItem('atguigu-inspect-session-id'", template)
