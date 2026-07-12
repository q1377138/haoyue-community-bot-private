# Operations Boundary

## The Bot May Do

- Reply to community-binding commands: `绑定`, `绑定状态`, `我的绑定`, and `我的权益`.
- Reply to base-weekly-welfare commands: `周福利`, `福利规则`, and `余额福利`.
- Check binding status from approved read-only sources.
- Generate read-only base weekly welfare eligibility previews.
- Mark a reviewed base payout plan only after the owner approves the real balance change.

## Base Weekly Welfare

- Community binding must be effective.
- Live Sub2API balance must be strictly greater than `10` at settlement time.
- Reward is exactly `2` balance once per eligible user per week.
- Every payout requires a backup, a transaction, and balance-ledger verification.

## Disabled Behavior

- Sign-in and streaks.
- Points, weekly points, rankings, and rank rewards.
- Lottery tickets, draws, blind boxes, wheels, and lucky bags.
- Cultivation, PvP, world boss, starship, market, and all other games.
- Menus, support-keyword replies, owner-mention replies, and unrelated automatic replies.
- Variable or activity-score-based payout plans.

Legacy game data remains stored for audit and rollback purposes, but no command may read, mutate, award, spend, rank, or clear it.

## Production Safety

- Do not change balances, points, coupons, or binding state without explicit owner approval.
- Do not reconnect RAG or knowledge-base services.
- Do not ingest private messages into a knowledge index.
- Back up the deployed source and state before every production edit.
