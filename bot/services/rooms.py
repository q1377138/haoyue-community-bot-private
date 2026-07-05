from __future__ import annotations

from dataclasses import dataclass

from bot.settings import (
    BOT_DEVELOPMENT_RULES_URL,
    DAILY_SUMMARY_ROOMS,
    DAILY_SUMMARY_TIME,
    DAILY_SUMMARY_TIMEZONE,
    PRIMARY_COMMUNITY_ROOM_ID,
    PRIMARY_COMMUNITY_ROOM_URL,
)


@dataclass(frozen=True)
class CommunityRoom:
    id: str
    url: str


def primary_room() -> CommunityRoom:
    return CommunityRoom(PRIMARY_COMMUNITY_ROOM_ID, PRIMARY_COMMUNITY_ROOM_URL)


def daily_summary_rooms() -> list[CommunityRoom]:
    return [CommunityRoom(room_id, url) for room_id, url in DAILY_SUMMARY_ROOMS]


def daily_summary_schedule() -> dict[str, object]:
    return {
        "time": DAILY_SUMMARY_TIME,
        "timezone": DAILY_SUMMARY_TIMEZONE,
        "rooms": [room.__dict__ for room in daily_summary_rooms()],
        "development_rules_url": BOT_DEVELOPMENT_RULES_URL,
    }

