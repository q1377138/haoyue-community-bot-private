# Paid User Label

## Rule

Do not show internal group names such as `free_community` to users.

For community benefit panels:

- `total_recharged > 0` -> `付费用户`
- `total_recharged <= 0` or missing -> `白嫖用户`

This label is only a display label. It must not change balance, group permission, model access, or payout eligibility by itself.

## Production Source

The authoritative source for real recharge status is the transfer-station `users.total_recharged` field.

The community bot sync flow enriches approved community binding records with `total_recharged`, then writes:

- `communityBinding.totalRecharged`
- `communityBinding.hasRealRecharge`
- `communityBinding.userType`

