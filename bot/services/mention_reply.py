from __future__ import annotations

import re

from bot.settings import OWNER_MENTION_NAME, OWNER_MENTION_REPLY

SERVICE_SUPPORT_RE = re.compile(
    r"(报错|错误|失败|不稳定|卡顿|断流|超时|充值|USDT|余额|额度|模型|分组|令牌|密钥|key|api|base\s*url|接口|接入|价格|倍率|套餐|订阅|购买|付款|支付|Claude Code|Codex|Gemini|OpenAI|Responses|403|401|429|502|503|504|522)",
    re.IGNORECASE,
)
CASUAL_MENTION_RE = re.compile(r"(奥特曼|变身|签到|打卡|哈哈|测试|test)", re.IGNORECASE)


def owner_mention_question(text: str) -> str:
    return (text or "").replace(OWNER_MENTION_NAME, "").strip(" ，,。:：")


def owner_mention_reply(text: str) -> str | None:
    if OWNER_MENTION_NAME in (text or ""):
        return OWNER_MENTION_REPLY
    return None


def owner_mention_requires_knowledge(text: str) -> bool:
    question = owner_mention_question(text)
    return OWNER_MENTION_NAME in (text or "") and len(question) >= 2 and SERVICE_SUPPORT_RE.search(question) is not None


def owner_mention_is_casual(text: str) -> bool:
    question = owner_mention_question(text)
    return OWNER_MENTION_NAME in (text or "") and CASUAL_MENTION_RE.search(question) is not None
