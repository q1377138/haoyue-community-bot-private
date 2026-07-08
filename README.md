# Haoyue Community Bot

Private repository for Haoyue community bot operating rules, checks, and support helpers.

This bot is responsible for community-facing automation only. It must not own Sub2API routing, model availability, upstream account cooldowns, or billing database changes unless explicitly approved by the owner.

## Scope

- Community service group buttons and links.
- `dc.hhhl.cc` community room automation.
- Community binding checks.
- Weekly welfare notice and eligibility reports.
- Daily 03:00 community room information collection and summary.
- Weekly points/ranking announcement helpers.
- Fixed/local support auto-replies and community operation helpers.

## Hard Boundaries

- No real bot token, production database password, SSH key, or user export may be committed.
- Welfare payout actions must be generated as reviewable plans first.
- Any action that changes user balance, points, coupons, or group binding state requires explicit owner approval.
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
