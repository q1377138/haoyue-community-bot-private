from __future__ import annotations

from bot.settings import FREE_USER_LABEL, PAID_USER_LABEL


def user_type_label(total_recharged: float | int | str | None) -> str:
    try:
        amount = float(total_recharged or 0)
    except (TypeError, ValueError):
        amount = 0
    return PAID_USER_LABEL if amount > 0 else FREE_USER_LABEL

