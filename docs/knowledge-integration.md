# Knowledge Integration

## Current Production Reality

Read-only check on `43.155.168.147` showed the production community bot is a Node/Docker service under `/opt/haoyue-community-bot`.

The running bot already has a local Markdown knowledge layer:

- source directory: `/opt/haoyue-community-bot/docs/knowledge`
- trigger examples: `知识库`, `帮助中心`, `查教程`, `查FAQ`, `查报错`
- daily summary cron: `0 3 * * * /opt/haoyue-community-bot/scripts/run-community-learn-report.sh`
- summary sync script: `scripts/sync-community-learn-knowledge.mjs`
- generated local knowledge file: `docs/knowledge/09-community-learn-summary.md`

The central RAG server on `216.195.211.69` listens on `127.0.0.1:18080`, not on a public interface. A read-only check from `43.155.168.147` to `216.195.211.69:18080` timed out. This is safer than exposing RAG directly.

## Recommended Integration Mode

Use a local public-knowledge mirror inside the bot for live group replies.

Flow:

```text
central reviewed knowledge / public docs
  -> bot docs/knowledge mirror
  -> local keyword retrieval in bot
  -> community reply
```

Daily community learning flow:

```text
two community rooms at 03:00
  -> local report JSON/MD on bot server
  -> redacted summary knowledge file
  -> local bot knowledge mirror
  -> optional reviewed sync to central RAG
```

## Why Not Directly Expose RAG

- RAG contains private ops material and is shared by multiple agents.
- Community users should only see public/support-safe knowledge.
- Opening `18080` directly would bypass existing RAG access boundaries.
- The bot can answer fast using local Markdown without adding a network dependency.

## Direct RAG Access Requirement

If later live central RAG query is required, use one of these approved designs:

- HTTPS endpoint on RAG server with token auth and firewall allowlist only for `43.155.168.147`.
- SSH tunnel with a restricted key and read-only `/search` access.
- Reverse proxy sidecar that exposes only `public` documents.

Do not expose raw `/search` publicly without owner approval.

