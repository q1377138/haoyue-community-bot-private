import unittest

from bot.services.tg_links import service_group_button


class TgLinkTests(unittest.TestCase):
    def test_service_group_label_and_url_are_canonical(self):
        button = service_group_button()
        self.assertEqual(button.label, "TG服务群")
        self.assertEqual(button.url, "https://t.me/+s485tyl24600YzAx")


if __name__ == "__main__":
    unittest.main()

