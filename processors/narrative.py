from __future__ import annotations

import re


def generate_narrative(text: str) -> str:
    """Create a lightly paced, faithful voiceover version without adding facts."""
    paragraphs = re.split(r"\n\s*\n", text.strip())
    polished = []
    for paragraph in paragraphs:
        paragraph = re.sub(r"[ \t]+", " ", paragraph).strip()
        if not paragraph:
            continue
        paragraph = re.sub(r"\s*([,;:])\s*", r"\1 ", paragraph)
        paragraph = re.sub(r"\s*([.!?])\s*", r"\1\n", paragraph)
        polished.append(paragraph.strip())
    return "\n\n".join(polished) + "\n"
