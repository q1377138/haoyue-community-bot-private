from __future__ import annotations

from dataclasses import dataclass

from bot.settings import WEEKLY_MINIMUM_BALANCE, WEEKLY_REWARD_BALANCE


@dataclass(frozen=True)
class WelfareEligibility:
    eligible: bool
    reward_balance: int
    reason: str


def evaluate_weekly_welfare(balance: float, community_bound: bool) -> WelfareEligibility:
    if balance <= WEEKLY_MINIMUM_BALANCE:
        return WelfareEligibility(False, 0, "balance_not_greater_than_10")
    if not community_bound:
        return WelfareEligibility(False, 0, "community_not_bound")
    return WelfareEligibility(True, WEEKLY_REWARD_BALANCE, "eligible")

