from __future__ import annotations

import re

WORDS_PER_SECOND = 2.5
MAX_WORDS_PER_CAPTION = 11


def _timestamp(seconds: float) -> str:
    total_ms = int(seconds * 1000)
    hours, remaining = divmod(total_ms, 3_600_000)
    minutes, remaining = divmod(remaining, 60_000)
    secs, ms = divmod(remaining, 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{ms:03}"


def generate_subtitles(text: str) -> str:
    words = re.findall(r"\S+", text)
    captions = [words[i:i + MAX_WORDS_PER_CAPTION] for i in range(0, len(words), MAX_WORDS_PER_CAPTION)]
    blocks = []
    position = 0.0
    for number, caption in enumerate(captions, start=1):
        duration = max(1.2, len(caption) / WORDS_PER_SECOND)
        blocks.append(f"{number}\n{_timestamp(position)} --> {_timestamp(position + duration)}\n{' '.join(caption)}")
        position += duration
    return "\n\n".join(blocks) + "\n"
