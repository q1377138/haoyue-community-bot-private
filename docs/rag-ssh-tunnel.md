# RAG SSH Tunnel

## Purpose

The community bot on `43.155.168.147` can query the central RAG on `216.195.211.69` through a local SSH tunnel without exposing the RAG port publicly.

## Current Production State

Implemented on 2026-07-06:

- Source host: `43.155.168.147`
- Source user: `ubuntu`
- Local tunnel endpoint on 43: `http://127.0.0.1:18080`
- Destination host: `216.195.211.69`
- Destination RAG endpoint: `127.0.0.1:18080`
- Systemd unit on 43: `haoyue-rag-tunnel.service`
- Tunnel key on 43: `/home/ubuntu/.ssh/haoyue_rag_tunnel_ed25519`
- Key comment: `haoyue-rag-tunnel-43-to-216-20260706`

## Security Boundary

The key added to `216.195.211.69:/root/.ssh/authorized_keys` is restricted:

```text
command="/bin/false",from="43.155.168.147",no-agent-forwarding,no-X11-forwarding,no-pty,permitopen="127.0.0.1:18080"
```

This means the key is only for the tunnel and cannot be used for an interactive shell.

## Operations

Check service:

```bash
systemctl status haoyue-rag-tunnel.service --no-pager
```

Check local endpoint from the bot server:

```bash
curl -fsS http://127.0.0.1:18080/health
curl -fsS --get --data-urlencode q=RebuildLock --data-urlencode k=2 http://127.0.0.1:18080/search
```

Restart tunnel:

```bash
sudo systemctl restart haoyue-rag-tunnel.service
```

Disable tunnel:

```bash
sudo systemctl disable --now haoyue-rag-tunnel.service
```

## Important

- Do not expose `216.195.211.69:18080` publicly.
- Do not forward `/admin/rebuild` to customers.
- Community bot usage should prefer public/support-safe queries.
- Raw community messages must not be pushed to central RAG without redaction and review.

