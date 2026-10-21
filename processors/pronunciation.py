from __future__ import annotations

import json
import re
from pathlib import Path

DICTIONARY_FILE = Path(__file__).resolve().parent.parent / "data" / "pronunciation_dictionary.json"


def load_default_dictionary() -> dict[str, str]:
    try:
        with DICTIONARY_FILE.open(encoding="utf-8") as file:
            data = json.load(file)
        return {str(key): str(value) for key, value in data.items()}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def parse_custom_dictionary(raw: str) -> dict[str, str]:
    """Parse one `original = spoken form` pair per line, ignoring invalid rows."""
    result: dict[str, str] = {}
    for line in raw.splitlines():
        if "=" not in line:
            continue
        source, replacement = (part.strip() for part in line.split("=", 1))
        if source and replacement:
            result[source] = replacement
    return result


def apply_pronunciations(text: str, custom: dict[str, str] | None = None) -> tuple[str, list[dict[str, str | int]]]:
    dictionary = {**load_default_dictionary(), **(custom or {})}
    changes: list[dict[str, str | int]] = []
    output = text
    # Longest terms first prevents a short entry changing part of a longer term.
    for source in sorted(dictionary, key=len, reverse=True):
        replacement = dictionary[source]
        pattern = re.compile(r"(?<!\w)" + re.escape(source) + r"(?!\w)", re.IGNORECASE)
        # A function replacement inserts the spoken form literally. Passing the
        # replacement as a string makes re.sub interpret backslashes as group
        # references, so an entry such as "C:\path" raised re.error.
        output, count = pattern.subn(lambda _match, value=replacement: value, output)
        if count:
            changes.append({"from": source, "to": replacement, "count": count})
    return output, changes
