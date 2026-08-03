import unittest
from copy import deepcopy

from atguigu_ai.core.domain import Domain
from atguigu_ai.core.stores.json_store import JsonTrackerStore
from atguigu_ai.core.tracker import DialogueStateTracker
from atguigu_ai.dialogue_understanding.commands.slot_commands import SetSlotCommand


class UserProfilePersistenceTest(unittest.IsolatedAsyncioTestCase):
    async def test_set_slot_survives_json_tracker_reload(self) -> None:
        domain = Domain.from_dict(
            {
                "slots": {
                    "user_name": {
                        "type": "text",
                        "mappings": [{"type": "from_llm"}],
                    }
                }
            }
        )
        tracker = DialogueStateTracker(
            sender_id="user-1",
            slots=deepcopy(domain.slots),
        )
        SetSlotCommand(name="user_name", value="jr").run(tracker)

        store = JsonTrackerStore(domain=domain, in_memory=True)
        await store.save(tracker)
        restored = await store.retrieve("user-1")

        self.assertIsNotNone(restored)
        self.assertEqual("jr", restored.get_slot("user_name"))


if __name__ == "__main__":
    unittest.main()
