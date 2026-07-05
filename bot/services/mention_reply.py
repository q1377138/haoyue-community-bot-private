from __future__ import annotations

from bot.settings import OWNER_MENTION_NAME, OWNER_MENTION_REPLY


def owner_mention_question(text: str) -> str:
    return (text or "").replace(OWNER_MENTION_NAME, "").strip(" ，,。:：")


def owner_mention_reply(text: str) -> str | None:
    if OWNER_MENTION_NAME in (text or ""):
        return OWNER_MENTION_REPLY
    return None


def owner_mention_requires_knowledge(text: str) -> bool:
    return OWNER_MENTION_NAME in (text or "") and len(owner_mention_question(text)) >= 2

