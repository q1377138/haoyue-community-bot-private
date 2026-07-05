from __future__ import annotations

from bot.settings import OWNER_MENTION_NAME, OWNER_MENTION_REPLY


def owner_mention_reply(text: str) -> str | None:
    if OWNER_MENTION_NAME in (text or ""):
        return OWNER_MENTION_REPLY
    return None

