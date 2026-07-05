from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


DEFAULT_DICTIONARY = (
    "key",
    "token",
    "api",
    "base",
    "url",
    "claude",
    "codex",
    "gemini",
    "充值",
    "支付",
    "余额",
    "额度",
    "周福利",
    "绑定",
    "抽奖券",
    "报错",
    "错误",
    "429",
    "502",
    "503",
    "403",
    "401",
    "504",
    "模型",
    "分组",
    "plus",
    "pro",
    "教程",
    "接入",
    "社区服务群",
    "令牌",
    "密钥",
    "价格",
    "倍率",
    "首充",
    "套餐",
    "权限",
    "稳定",
    "限流",
)


@dataclass(frozen=True)
class KnowledgeDoc:
    name: str
    title: str
    keywords: tuple[str, ...]
    text: str


@dataclass(frozen=True)
class KnowledgeHit:
    name: str
    title: str
    score: int
    snippet: str


def load_knowledge_docs(root: Path) -> list[KnowledgeDoc]:
    if not root.exists():
        return []
    docs: list[KnowledgeDoc] = []
    for path in sorted(root.glob("*.md")):
        if ".bak-" in path.name:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        title_match = re.search(r"^#\s+(.+)$", text, re.M)
        keyword_match = re.search(r"^关键词[:：]\s*(.+)$", text, re.M)
        title = title_match.group(1).strip() if title_match else path.stem
        keywords = tuple(x for x in re.split(r"[、,，\s]+", keyword_match.group(1).strip() if keyword_match else "") if x)
        docs.append(KnowledgeDoc(path.name, title, keywords, text))
    return docs


def knowledge_terms(raw: str) -> list[str]:
    text = (raw or "").lower()
    terms = set(x for x in re.split(r"[^a-z0-9\u4e00-\u9fa5]+", text, flags=re.I) if len(x) >= 2)
    for word in DEFAULT_DICTIONARY:
        if word.lower() in text:
            terms.add(word.lower())
    return sorted(terms)


def snippet_for(text: str, terms: list[str], limit: int = 96) -> str:
    lines = [x.strip() for x in text.splitlines() if x.strip() and not x.startswith("#") and not x.startswith("关键词")]
    hit = next((line for line in lines if any(term in line.lower() for term in terms)), lines[0] if lines else "")
    return re.sub(r"^[-*]\s*", "", hit)[:limit]


def search_knowledge(query: str, root: Path, limit: int = 3) -> list[KnowledgeHit]:
    docs = load_knowledge_docs(root)
    terms = knowledge_terms(query)
    rows: list[KnowledgeHit] = []
    lowered_query = (query or "").lower()
    for doc in docs:
        hay = f"{doc.title}\n{' '.join(doc.keywords)}\n{doc.text}".lower()
        score = 0
        for term in terms:
            if term in doc.title.lower():
                score += 5
            if any(term in keyword.lower() for keyword in doc.keywords):
                score += 4
            if term in hay:
                score += 1
        if lowered_query and lowered_query in hay:
            score += 3
        if score > 0:
            rows.append(KnowledgeHit(doc.name, doc.title, score, snippet_for(doc.text, terms)))
    return sorted(rows, key=lambda x: (-x.score, x.name))[:limit]

