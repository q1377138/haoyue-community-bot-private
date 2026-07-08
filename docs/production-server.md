# Production Server

## Host

- IP: `43.155.168.147`
- Login: `ubuntu`
- SSH key: `nube_sjc_ed25519`
- Project label from owner: `haoyue_bot_seoul`
- Observed deployment path: `/opt/haoyue-community-bot`

## Current Runtime Observation

- `ubuntu@43.155.168.147` login works with Git SSH and `nube_sjc_ed25519`.
- `haoyue-community-bot.service` exists.
- The service runs Docker Compose from `/opt/haoyue-community-bot`.
- Container name: `haoyue-community-bot`.
- Image: `node:24-alpine`.
- Compose timezone: `Asia/Shanghai`.
- Main source file observed in production: `/opt/haoyue-community-bot/src/bot.mjs`.

## Knowledge/RAG State

As of 2026-07-09:

- the old central RAG server was deleted.
- `haoyue-rag-tunnel.service` is inactive and disabled.
- the bot must not depend on `127.0.0.1:18080`.
- the bot should answer owner mentions with fixed/local support rules only.

## Deployment Boundary

Do not overwrite production files from this repository until the existing Node bot source has been safely imported or a migration plan is approved.

Before any production edit:

1. Back up the target file on the server.
2. Patch only the required file.
3. Restart only `haoyue-community-bot`.
4. Verify logs, room connection, and adjacent room behavior.
