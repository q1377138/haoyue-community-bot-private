# Haoyue Community Bot

Private repository for Haoyue community bot operating rules, checks, and support helpers.

This bot is responsible for community-facing automation only. It must not own Sub2API routing, model availability, upstream account cooldowns, or billing database changes unless explicitly approved by the owner.

## Scope

- Community binding guidance and binding-status checks.
- Base weekly welfare notices and eligibility reports.
- Base weekly welfare rule: effective community binding, live balance strictly greater than `10`, reward exactly `2` once per week.

All games and unrelated automatic replies are disabled, including sign-in, points, cultivation, rankings, rank rewards, lottery tickets, draws, starship, PvP, market, daily tasks, support auto-replies, and owner-mention replies.

## Hard Boundaries

- No real bot token, production database password, SSH key, or user export may be committed.
- Welfare payout actions must be generated as reviewable plans first.
- Any action that changes user balance, points, coupons, or group binding state requires explicit owner approval.
- Variable game/rank payout plans are forbidden. Only an externally verified `*-base-2yuan` plan with amount exactly `2` per eligible user may be marked paid.
- The canonical service group label is `社区服务群`.
- The canonical service group URL is `https://t.me/+s485tyl24600YzAx`.
- Main served community room: `https://dc.hhhl.cc/chat/room/ani5vmvdqm`.
- Daily summary rooms: `ani5vmvdqm` and `amlc1bekzi`.
- Development rules page: `https://dc.hhhl.cc/settings/connect`.
- Production bot host: `ubuntu@43.155.168.147`, project name `haoyue_bot_seoul`, deployed path currently observed as `/opt/haoyue-community-bot`.
- Knowledge/RAG integration is cancelled. Do not reconnect RAG, recreate `haoyue-rag-tunnel.service`, or call `127.0.0.1:18080` unless the owner explicitly restores the knowledge server.

## Local Checks

```powershell
python -m unittest discover -s tests
python -m bot.cli weekly-preview --balance 12 --community-bound true
```
