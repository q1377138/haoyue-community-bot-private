# Haoyue Community Bot

Private repository for Haoyue community/TG bot code and operating rules.

This bot is responsible for community-facing automation only. It must not own Sub2API routing, model availability, upstream account cooldowns, or billing database changes unless explicitly approved by the owner.

## Scope

- Telegram service group buttons and links.
- dc.hhhl.cc community room automation.
- Community binding checks.
- Weekly welfare notice and eligibility reports.
- Daily 03:00 community room information collection and summary.
- Weekly points/ranking announcement helpers.
- Support auto-replies and community operation helpers.

## Hard Boundaries

- No real bot token, production database password, SSH key, or user export may be committed.
- Welfare payout actions must be generated as reviewable plans first.
- Any action that changes user balance, points, coupons, or group binding state requires explicit owner approval.
- The canonical service group label is `社区服务群`.
- The canonical TG service group URL is `https://t.me/+s485tyl24600YzAx`.
- Main served community room: `https://dc.hhhl.cc/chat/room/ani5vmvdqm`.
- Daily summary rooms: `ani5vmvdqm` and `amlc1bekzi`.
- Development rules page: `https://dc.hhhl.cc/settings/connect`.
- Production bot host: `ubuntu@43.155.168.147`, project name `haoyue_bot_seoul`, deployed path currently observed as `/opt/haoyue-community-bot`.

## Local Checks

```powershell
python -m unittest discover -s tests
python -m bot.cli weekly-preview --balance 12 --community-bound true
```
