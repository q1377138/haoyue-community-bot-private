import unittest

from bot.services.rooms import daily_summary_schedule, primary_room


class RoomRuleTests(unittest.TestCase):
    def test_primary_room_is_ani5vmvdqm(self):
        room = primary_room()
        self.assertEqual(room.id, "ani5vmvdqm")
        self.assertEqual(room.url, "https://dc.hhhl.cc/chat/room/ani5vmvdqm")

    def test_daily_summary_has_two_rooms_at_3am(self):
        schedule = daily_summary_schedule()
        self.assertEqual(schedule["time"], "03:00")
        self.assertEqual(schedule["timezone"], "Asia/Shanghai")
        self.assertEqual(
            [room["id"] for room in schedule["rooms"]],
            ["ani5vmvdqm", "amlc1bekzi"],
        )
        self.assertEqual(
            schedule["development_rules_url"],
            "https://dc.hhhl.cc/settings/connect",
        )


if __name__ == "__main__":
    unittest.main()

