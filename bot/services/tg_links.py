from __future__ import annotations

from dataclasses import dataclass

from bot.settings import TG_SERVICE_GROUP_LABEL, TG_SERVICE_GROUP_URL


@dataclass(frozen=True)
class LinkButton:
    label: str
    url: str


def service_group_button() -> LinkButton:
    return LinkButton(label=TG_SERVICE_GROUP_LABEL, url=TG_SERVICE_GROUP_URL)

