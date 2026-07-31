from __future__ import annotations

import re


def generate_blog(text: str) -> str:
    paragraphs = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    title = next((p for p in paragraphs if len(p) < 90), "A practical guide")
    title = re.sub(r"[.!?]+$", "", title)
    body = "\n\n".join(paragraphs)
    return f"# {title}\n\n## Overview\n\n{body}\n\n## Key takeaways\n\n" + "\n".join(f"- {item}" for item in _takeaways(text)) + "\n"


def _takeaways(text: str) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text).strip())
    return [sentence.strip() for sentence in sentences[:5] if sentence.strip()]
