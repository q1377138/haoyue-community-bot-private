import unittest

from bot.services.user_type import user_type_label


class UserTypeTests(unittest.TestCase):
    def test_paid_user_label(self):
        self.assertEqual(user_type_label(0.01), "付费用户")
        self.assertEqual(user_type_label("10"), "付费用户")

    def test_free_user_label(self):
        self.assertEqual(user_type_label(0), "白嫖用户")
        self.assertEqual(user_type_label(None), "白嫖用户")
        self.assertEqual(user_type_label(""), "白嫖用户")


if __name__ == "__main__":
    unittest.main()

