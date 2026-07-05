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
7. Clear weekly points and lottery coupons only after owner approval.

## Important

If a user appears bound in UI but binding is not confirmed in the real source, do not pay automatically. Put the account into manual review.

