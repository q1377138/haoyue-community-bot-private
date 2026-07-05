# Owner Mention Reply

## Rule

When a community room message explicitly contains:

```text
@q13771388
```

the bot replies with:

```text
皓悦 API 竭诚为您服务
```

## Production Hotfix

Implemented on `43.155.168.147` on 2026-07-06.

Backups before the hotfix:

- `/opt/haoyue-community-bot/src/bot.mjs.bak-owner-mention-20260706-004608`
- `/opt/haoyue-community-bot/src/bot.mjs.bak-owner-mention-fix-20260706-004638`

The production Node bot uses:

```js
const OWNER_MENTION_NAME = '@q13771388';
const OWNER_MENTION_REPLY = '皓悦 API 竭诚为您服务';
```

and checks this before the headquarters-room no-auto-reply guard, so a direct owner mention gets the fixed response.

