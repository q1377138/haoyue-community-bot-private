# Owner Mention Reply

## Rule

Both community rooms support owner mention replies.

When a community room message only explicitly contains:

```text
@q13771388
```

the bot replies with:

```text
皓悦 API 竭诚为您服务
```

When the message contains `@q13771388` plus a question, the production bot should query the knowledge base and answer from public/support-safe hits.

Examples:

```text
@q13771388 帮我看下403是怎么回事
@q13771388 Claude Code 怎么接入
```

## Room Behavior

- `ani5vmvdqm`: keep the existing automatic game/welfare/menu/service keyword replies.
- `amlc1bekzi`: do not auto-reply normally; reply only when explicitly mentioned.
- Both rooms: explicit `@q13771388` is allowed.

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

Updated on 2026-07-06:

- mention with question uses central RAG through the SSH tunnel at local `127.0.0.1:18080`
- RAG results are filtered to public/support-safe paths before being sent to the group
- empty mention still returns the fixed sentence

