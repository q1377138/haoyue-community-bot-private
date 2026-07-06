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

When the message contains `@q13771388` plus a question, the production bot may query the knowledge base internally, but the group-facing reply must look like a normal support answer from `皓悦小助手`.

Do not expose implementation wording such as `知识库`, `检索结果`, score, file names, paths, or hit lists in the group reply.

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
- RAG results are filtered to public/support-safe paths before being used
- group-facing answers use the title `皓悦小助手` and direct support wording only
- common short questions such as `我要key`, `403`, `401`, `429`, and `502/504` use fixed customer-support style answers first
- empty mention still returns the fixed sentence

Production user-facing hotfix on 2026-07-06:

- Backup: `/opt/haoyue-community-bot/src/bot.mjs.bak-user-facing-helper-*`
- Changed `centralRagCard()` and `knowledgeGuide()` so external replies no longer show `皓悦知识库 · 检索结果`.

Production reply-thread hotfix on 2026-07-06:

- Backup: `/opt/haoyue-community-bot/src/bot.mjs.bak-reply-thread-*`
- Tracks support-message IDs in `state.supportThreadMessageIds`.
- If a user replies to a `皓悦小助手` support answer, the bot treats the new message as a follow-up support question.
- Short greetings such as `@q13771388 在` now answer with a natural `在的，你直接说问题就行。` support prompt.

Production multi-room hotfix on 2026-07-06:

- Backup: `/opt/haoyue-community-bot/src/bot.mjs.bak-multiroom-*` and `src/bot.mjs.bak-multiroom-mentionid-*`.
- The live bot now connects to both `ani5vmvdqm` and `amlc1bekzi` instead of only `config.roomId`.
- Replies are sent back to the triggering message's `toRoomId`, not always the default room.
- Headquarters room still blocks normal automatic replies; it only handles owner mentions or support reply threads.
- Owner mention detection checks both literal `@q13771388` text and `mentionedUserIds` containing the bot account id.

Production intent-guard hotfix on 2026-07-06:

- Backup: `/opt/haoyue-community-bot/src/bot.mjs.bak-owner-intent-*`.
- `@q13771388` no longer sends every two-character message to RAG.
- Only service-support questions such as API Key, recharge, model, group, integration, latency, or error codes query RAG.
- Casual/game mentions such as `变身奥特曼` or `签到` receive short natural replies instead of fake troubleshooting cards.
- RAG no-hit replies must say that no reliable answer was found; they must not invent entry/model/report-time suggestions for unrelated chat.
