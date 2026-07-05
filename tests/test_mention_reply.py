import unittest

from bot.services.mention_reply import owner_mention_reply


class MentionReplyTests(unittest.TestCase):
    def test_owner_mention_gets_fixed_reply(self):
        self.assertEqual(
            owner_mention_reply("@q13771388"),
            "皓悦 API 竭诚为您服务",
        )

    def test_other_text_does_not_reply(self):
        self.assertIsNone(owner_mention_reply("你好"))


if __name__ == "__main__":
    unittest.main()

