# Development Rules

## Canonical Rule Source

- `https://dc.hhhl.cc/settings/connect`

This page is the source of product-side bot connection and development rules. When behavior conflicts with old local notes, verify this page first.

## Primary Service Target

The bot currently mainly serves:

- `https://dc.hhhl.cc/chat/room/ani5vmvdqm`

## Daily Community Summary

Every day at `03:00 Asia/Shanghai`, collect and summarize information from:

- `https://dc.hhhl.cc/chat/room/ani5vmvdqm`
- `https://dc.hhhl.cc/chat/room/amlc1bekzi`

The summary should distinguish:

- user questions and complaints
- stability or payment feedback
- useful product ideas
- support issues requiring follow-up
- candidate knowledge that may be sent to RAG after review

## Safety

- Do not publish summaries to users automatically before the owner approves the format.
- Do not store private raw conversations in GitHub.
- If summaries are later synced to RAG, sync only redacted/generalized knowledge.

