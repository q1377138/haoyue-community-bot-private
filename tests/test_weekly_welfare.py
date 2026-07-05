import unittest

from bot.services.weekly_welfare import evaluate_weekly_welfare


class WeeklyWelfareTests(unittest.TestCase):
    def test_balance_must_be_greater_than_10(self):
        result = evaluate_weekly_welfare(10, True)
        self.assertFalse(result.eligible)
        self.assertEqual(result.reason, "balance_not_greater_than_10")

    def test_binding_is_required(self):
        result = evaluate_weekly_welfare(12, False)
        self.assertFalse(result.eligible)
        self.assertEqual(result.reason, "community_not_bound")

    def test_eligible_user_gets_two_balance(self):
        result = evaluate_weekly_welfare(12, True)
        self.assertTrue(result.eligible)
        self.assertEqual(result.reward_balance, 2)


if __name__ == "__main__":
    unittest.main()

