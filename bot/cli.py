from __future__ import annotations

import argparse
import json

from bot.services.mention_reply import owner_mention_reply
from bot.services.rooms import daily_summary_schedule
from bot.services.tg_links import service_group_button
from bot.services.weekly_welfare import evaluate_weekly_welfare


def parse_bool(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "y"}:
        return True
    if normalized in {"0", "false", "no", "n"}:
        return False
    raise argparse.ArgumentTypeError(f"invalid boolean: {value}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Haoyue community bot utilities.")
    sub = parser.add_subparsers(dest="command", required=True)

    weekly = sub.add_parser("weekly-preview", help="Preview base weekly welfare eligibility.")
    weekly.add_argument("--balance", type=float, required=True)
    weekly.add_argument("--community-bound", type=parse_bool, required=True)

    sub.add_parser("service-group-button", help="Show canonical TG service group button.")
    sub.add_parser("daily-summary-schedule", help="Show canonical daily community summary schedule.")
    mention = sub.add_parser("mention-reply", help="Preview fixed owner mention reply.")
    mention.add_argument("text")

    args = parser.parse_args()
    if args.command == "weekly-preview":
        result = evaluate_weekly_welfare(args.balance, args.community_bound)
        print(json.dumps(result.__dict__, ensure_ascii=False))
        return 0
    if args.command == "service-group-button":
        button = service_group_button()
        print(json.dumps(button.__dict__, ensure_ascii=False))
        return 0
    if args.command == "daily-summary-schedule":
        print(json.dumps(daily_summary_schedule(), ensure_ascii=False))
        return 0
    if args.command == "mention-reply":
        print(json.dumps({"reply": owner_mention_reply(args.text)}, ensure_ascii=False))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
