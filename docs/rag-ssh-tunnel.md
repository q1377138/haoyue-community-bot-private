# RAG SSH Tunnel Cancelled

The previous SSH tunnel design is no longer active.

## Cancelled State

- Old RAG host: `216.195.211.69`
- Old local endpoint: `http://127.0.0.1:18080`
- Old systemd unit: `haoyue-rag-tunnel.service`
- Status on community bot server: inactive and disabled

## Hard Rule

Do not recreate this unit or open a replacement RAG port unless the owner explicitly restores the knowledge server.

If a future RAG service is approved, create a new design document first and require:

- token authentication
- IP allowlist or SSH tunnel
- public/support-only document scope
- no raw private conversation ingestion without review
