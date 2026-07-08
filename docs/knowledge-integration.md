# Knowledge Integration Cancelled

## Current Decision

As of 2026-07-09, the central knowledge/RAG server has been deleted by the owner.

The community bot must not depend on:

- `216.195.211.69`
- `127.0.0.1:18080`
- `haoyue-rag-tunnel.service`
- live RAG search
- knowledge rebuild endpoints
- raw prompt/response knowledge ingestion

## Production State

On `43.155.168.147`, the tunnel was disabled:

```bash
sudo systemctl disable --now haoyue-rag-tunnel.service
```

Verified state:

- `haoyue-rag-tunnel.service`: inactive
- `haoyue-rag-tunnel.service`: disabled
- no bot reply should expose words such as knowledge base, retrieval, RAG, hit list, score, file path, or source path.

## Bot Reply Rule

For both rooms, `@q13771388` remains supported.

- Empty mention: reply `皓悦 API 竭诚为您服务`.
- Service question: answer with fixed/local support wording only.
- Unknown service issue: ask for entrance, model, error code, timestamp, and screenshot.
- Do not call central RAG.
- Do not tell users that a knowledge search is running.

## Future Re-enable Gate

Do not reintroduce RAG, tunnels, or knowledge ingestion unless the owner explicitly restores the knowledge server and approves a new access design.
