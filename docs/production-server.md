# Production Server

## Host

- IP: `43.155.168.147`
- Login: `ubuntu`
- SSH key: `nube_sjc_ed25519`
- Project label from owner: `haoyue_bot_seoul`
- Observed deployment path: `/opt/haoyue-community-bot`

## Current Runtime Observation

Read-only check on 2026-07-05:

- `ubuntu@43.155.168.147` login works with `nube_sjc_ed25519`.
- `haoyue-community-bot.service` exists and is enabled.
- The systemd unit runs Docker Compose from `/opt/haoyue-community-bot`.
- Container name: `haoyue-community-bot`.
- Image: `node:24-alpine`.
- Compose timezone: `Asia/Shanghai`.
- Existing npm scripts include `live`, `weekly-benefit-report`, `weekly-payout-plan`, `community-learn-report`, `knowledge-sync`, and `weekly-cycle-report`.

## Deployment Boundary

Do not overwrite production files from this repository until the existing Node bot source has been safely imported or a migration plan is approved.

