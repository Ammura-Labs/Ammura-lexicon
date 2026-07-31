from __future__ import annotations

import re


def generate_notes(text: str) -> str:
    sentences = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text).strip())
    selected = [sentence.strip() for sentence in sentences if len(sentence.split()) >= 4][:8]
    return "\n".join(f"• {sentence}" for sentence in selected) + "\n"
