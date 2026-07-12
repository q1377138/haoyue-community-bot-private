# Minimal Community Mode Migration

## Target Behavior

The production bot replies only to:

- `绑定`
- `绑定状态`
- `我的绑定`
- `我的权益`
- `周福利`
- `福利规则`
- `余额福利`

The weekly welfare rule is fixed:

- effective community binding
- live Sub2API balance strictly greater than `10`
- exactly `2` balance once per eligible user per week

All other commands and automatic replies are ignored. This includes sign-in, streaks, points, weekly rankings, rank rewards, lottery tickets, draws, cultivation, PvP, world boss, starship, market, daily tasks, menus, support keywords, owner mentions, and reply-thread support.

Legacy game state is retained for audit and rollback. The migration does not delete or clear points, weekly points, tickets, or other game data.

## Hash-Pinned Production Baseline

- `src/bot.mjs`: `7f0ad3d8680f46d3950e5831f01a5fad59da9a1e536e9b823f9580f2185e6efa`
- `scripts/weekly-payout-admin.mjs`: `8b268f4ddcc0e07324075eb6831d1b336ba5c7d059a5866c490822d900678293`

The patcher refuses any unrecognized baseline.

Expected patched hashes:

- `src/bot.mjs`: `46611485adfc47b880ed392f031cf399871051b8f8102c145865dc6b0a3f7163`
- `scripts/weekly-payout-admin.mjs`: `054e946014486d00207771482e76d84deaea1f942be3d7cb6c8a4c36e6201ba3`

## Deployment Gate

Do not deploy until the owner approves this migration plan and Claude completes a read-only review.

1. Back up `src/bot.mjs`, `scripts/weekly-payout-admin.mjs`, `data/state.json`, and root crontab.
2. Verify both baseline hashes.
3. Apply `scripts/patch_minimal_community_mode.py` to the production files.
4. Run `node --check` on both patched files.
5. Remove only the `run-community-learn-report.sh` root cron entry; preserve all unrelated cron entries.
6. Restart only `haoyue-community-bot`.
7. Verify the container is running and logs contain no fatal or syntax errors.
8. Verify `签到`, `排行`, and representative game commands produce no reply.
9. Verify binding and base-weekly-welfare commands still reply with the fixed `balance > 10`, `+2` rule.
10. Verify `weekly-payout-admin.mjs plan` rejects game/rank plans and `mark-paid` accepts only a non-empty `*-base-2yuan` plan with every amount exactly `2`.

## Rollback

Restore the backed-up source files and root crontab, restart only `haoyue-community-bot`, and verify its container and room connection. Do not restore or alter user balances as part of a bot-code rollback.
