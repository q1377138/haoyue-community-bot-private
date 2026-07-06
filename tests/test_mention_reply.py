import unittest

from bot.services.mention_reply import (
    owner_mention_is_casual,
    owner_mention_question,
    owner_mention_reply,
    owner_mention_requires_knowledge,
)


class MentionReplyTests(unittest.TestCase):
    def test_owner_mention_gets_fixed_reply(self):
        self.assertEqual(
            owner_mention_reply("@q13771388"),
            "皓悦 API 竭诚为您服务",
        )

    def test_other_text_does_not_reply(self):
        self.assertIsNone(owner_mention_reply("你好"))

    def test_mention_with_question_requires_knowledge(self):
        text = "@q13771388 帮我看下403是怎么回事"
        self.assertTrue(owner_mention_requires_knowledge(text))
        self.assertEqual(owner_mention_question(text), "帮我看下403是怎么回事")

    def test_empty_mention_does_not_require_knowledge(self):
        self.assertFalse(owner_mention_requires_knowledge("@q13771388"))

    def test_casual_mention_does_not_require_knowledge(self):
        text = "@q13771388 变身奥特曼"
        self.assertFalse(owner_mention_requires_knowledge(text))
        self.assertTrue(owner_mention_is_casual(text))

    def test_game_mention_does_not_require_knowledge(self):
        text = "@q13771388 签到"
        self.assertFalse(owner_mention_requires_knowledge(text))
        self.assertTrue(owner_mention_is_casual(text))


if __name__ == "__main__":
    unittest.main()
