# Weekly Welfare Workflow

## Rule

Users are eligible for base weekly welfare when:

- balance is greater than `10`
- community binding is confirmed

Default base reward:

- `2` balance

## Required Flow

1. Read-only eligibility preview.
2. Owner reviews the final list.
3. Generate a payout plan.
4. Owner explicitly approves payout.
5. Execute payout.
6. Record audit result.
7. Do not calculate or issue ranking rewards.
8. Do not clear or use legacy game points or lottery coupons; game features are disabled.

## Important

If a user appears bound in UI but binding is not confirmed in the real source, do not pay automatically. Put the account into manual review.

The production bot may only explain binding and this base weekly welfare rule. Sign-in, rankings, rank rewards, points, lottery tickets, and all other games are disabled.
