#!/usr/bin/env python3
"""Build daily newsletter from https://huggingface.co/papers/trending

Outputs:
- Creates/updates a daily note under `000 - daily notes/` with
  - Latest papers (filtered)
  - TLDR top papers (per-paper TLDR referencing which paper)
- Prints a Discord-ready TLDR message to stdout

Filtering is keyword-based and tuned to Batman's current interests
"""

from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

import urllib.request


HF_TRENDING_URL = "https://huggingface.co/papers/trending"

INTEREST_KEYWORDS = [
    # broad
    "large language model",
    "llm",
    "language model",
    "transformer",
    # RL for LLMs
    "reinforcement learning",
    "rlhf",
    "rlaif",
    "policy gradient",
    # specific
    "group relative policy optimization",
    "group relative policy optimisation",
    "grpo",
    "verifiable rewards",
    "rlvr",
]


@dataclass
class Paper:
    title: str
    url: str
    abstract: str | None
    arxiv: str | None


def fetch(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122 Safari/537.36",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "ignore")


def norm(s: str) -> str:
    s = s.lower()
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def matches_interest(text: str) -> bool:
    t = norm(text)
    return any(k in t for k in [norm(x) for x in INTEREST_KEYWORDS])


def extract_json_ld(html: str) -> list[dict]:
    out: list[dict] = []
    for m in re.finditer(r"<script[^>]+type=\"application/ld\+json\"[^>]*>(.*?)</script>", html, re.S):
        raw = m.group(1).strip()
        try:
            obj = json.loads(raw)
        except Exception:
            continue
        if isinstance(obj, list):
            out.extend([x for x in obj if isinstance(x, dict)])
        elif isinstance(obj, dict):
            out.append(obj)
    return out


def extract_arxiv_link(html: str) -> str | None:
    # prefer explicit arxiv links if present
    m = re.search(r"https?://arxiv\.org/abs/[0-9]{4}\.[0-9]{5}(v\d+)?", html)
    if m:
        return m.group(0)
    return None


def extract_title(html: str) -> str | None:
    # OpenGraph
    m = re.search(r"<meta[^>]+property=\"og:title\"[^>]+content=\"([^\"]+)\"", html)
    if m:
        return m.group(1)
    # <title>
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    if m:
        return re.sub(r"\s+", " ", m.group(1)).strip()
    return None


def parse_trending(html: str) -> list[Paper]:
    # HuggingFace pages are JS-heavy but include JSON-LD + normal anchors
    # Heuristic: collect paper links from /papers/ slug
    urls = []
    for m in re.finditer(r"href=\"(/papers/[^\"]+)\"", html):
        u = "https://huggingface.co" + m.group(1)
        if u not in urls:
            urls.append(u)

    papers: list[Paper] = []
    for u in urls[:50]:
        try:
            ph = fetch(u)
        except Exception:
            continue
        title = extract_title(ph) or u
        arxiv = extract_arxiv_link(ph)
        # crude abstract extraction
        abs_m = re.search(r"<meta[^>]+name=\"description\"[^>]+content=\"([^\"]+)\"", ph)
        abstract = abs_m.group(1) if abs_m else None
        papers.append(Paper(title=title, url=u, abstract=abstract, arxiv=arxiv))

    return papers


def today_str() -> str:
    # Use Europe/Amsterdam date if provided
    tz = os.environ.get("TZ", "Europe/Amsterdam")
    # If TZ isn't respected, still ok; date boundary is minor for daily note
    return datetime.now().strftime("%Y-%m-%d")


def daily_note_path(vault_root: Path) -> Path:
    d = today_str()
    return vault_root / "000 - daily notes" / f"{d}.md"


def short_summary(p: Paper) -> str:
    # Minimal, safe, no claims
    # Use description meta if present
    if p.abstract:
        s = p.abstract
        s = re.sub(r"\s+", " ", s).strip()
        # keep short
        if len(s) > 220:
            s = s[:217] + "..."
        return s
    return "summary pending"


def tldr_lines(papers: list[Paper]) -> list[str]:
    lines = []
    for i, p in enumerate(papers, 1):
        ref = p.arxiv or p.url
        # TLDR must cite which paper
        lines.append(f"{i}) {p.title} — {ref}")
    return lines


def render_daily_note(papers: list[Paper]) -> str:
    d = today_str()
    out = []
    out.append("---")
    out.append("tags:")
    out.append("- meta")
    out.append("description: ''")
    out.append("parent nodes:")
    out.append("- '[[research.base]]'")
    out.append("aliases: null")
    out.append("published on: null")
    out.append("---")
    out.append("")
    out.append(f"- Date: {d}")
    out.append("")
    out.append("## Latest papers")
    out.append("")
    if papers:
        for p in papers:
            ref = p.arxiv or p.url
            out.append(f"- [ ] [{p.title}]({ref})")
            out.append(f"\t- {short_summary(p)}")
    else:
        out.append("- [ ] none matched")
    out.append("")
    out.append("## TLDR top papers")
    out.append("")
    if papers:
        for line in tldr_lines(papers[:10]):
            out.append(f"- [ ] {line}")
    else:
        out.append("- [ ] none")
    out.append("")
    return "\n".join(out)


def main() -> int:
    vault_root = Path(__file__).resolve().parents[1]
    trending = fetch(HF_TRENDING_URL)
    papers = parse_trending(trending)

    # filter by interest
    filtered = []
    for p in papers:
        text = " ".join([p.title, p.abstract or "", p.arxiv or ""])
        if matches_interest(text):
            filtered.append(p)

    # write daily note
    note_path = daily_note_path(vault_root)
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(render_daily_note(filtered), encoding="utf-8")

    # discord message
    msg = []
    msg.append(f"Daily papers ({today_str()})")
    if filtered:
        msg.append("")
        msg.append("TLDR top papers")
        for line in tldr_lines(filtered[:10]):
            msg.append(line)
    else:
        msg.append("No trending papers matched current interests")

    sys.stdout.write("\n".join(msg) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
