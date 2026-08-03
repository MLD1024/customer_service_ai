import unittest
from copy import deepcopy

from atguigu_ai.core.domain import Domain
from atguigu_ai.core.tracker import DialogueStateTracker, UserMessage
from atguigu_ai.dialogue_understanding.flow import FlowsList
from atguigu_ai.dialogue_understanding.generator.prompt_builder import PromptBuilder


class PromptBuilderTest(unittest.TestCase):
    def test_prompt_exposes_global_slots_for_user_profile_memory(self) -> None:
        domain = Domain.from_dict(
            {
                "slots": {
                    "user_name": {
                        "type": "text",
                        "mappings": [{"type": "from_llm"}],
                        "description": "用户姓名",
                    }
                }
            }
        )
        tracker = DialogueStateTracker(
            sender_id="user-1",
            slots=deepcopy(domain.slots),
        )
        tracker.update_with_message(UserMessage(text="我叫 jr"))

        prompt = PromptBuilder().build_prompt(
            tracker=tracker,
            domain=domain,
            flows=FlowsList(),
        )

        self.assertIn('"name":"user_name"', prompt)
        self.assertIn("用户明确提供个人信息时，使用 `set slot` 保存", prompt)

    def test_prompt_does_not_expose_controlled_slots_to_llm(self) -> None:
        domain = Domain.from_dict(
            {
                "slots": {
                    "internal_user_id": {
                        "type": "text",
                        "mappings": [{"type": "controlled"}],
                    }
                }
            }
        )
        tracker = DialogueStateTracker(
            sender_id="user-1",
            slots=deepcopy(domain.slots),
        )
        tracker.update_with_message(UserMessage(text="你好"))

        prompt = PromptBuilder().build_prompt(
            tracker=tracker,
            domain=domain,
            flows=FlowsList(),
        )

        self.assertNotIn('"name":"internal_user_id"', prompt)


if __name__ == "__main__":
    unittest.main()
