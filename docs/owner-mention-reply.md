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

When the message contains `@q13771388` plus a service question, the bot must answer from fixed/local support rules only.

Do not expose implementation wording such as `知识库`, `检索结果`, `RAG`, score, file names, paths, or hit lists in the group reply.

Examples:

```text
@q13771388 帮我看下403是怎么回事
@q13771388 Claude Code 怎么接入
```

## Room Behavior

- `ani5vmvdqm`: keep the existing automatic game/welfare/menu/service keyword replies.
- `amlc1bekzi`: do not auto-reply normally; reply only when explicitly mentioned.
- Both rooms: explicit `@q13771388` is allowed.
- Both rooms: replying to a prior `皓悦小助手` support answer also continues the support conversation, even when the follow-up message does not repeat `@q13771388`.
- Replies to game/activity cards are not treated as support threads.

## Production Notes

Production host: `43.155.168.147`

On 2026-07-09, after the knowledge server was deleted:

- `haoyue-rag-tunnel.service` was disabled and stopped.
- `src/bot.mjs` was hotfixed so owner mentions no longer call central RAG.
- old user-facing knowledge commands no longer steal error-code support replies.
- log field `rag` was replaced with `support`.
- backup before hotfix: `/opt/haoyue-community-bot/src/bot.mjs.bak-disable-rag-20260709-062923`

Support questions should either match a direct fixed answer, or ask the user for entrance, model, error code, timestamp, and screenshot.
