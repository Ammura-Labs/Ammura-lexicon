from __future__ import annotations

from pathlib import Path


def generate_voiceover(text: str, destination: Path) -> str | None:
    text = text.strip()

    if not text:
        return "Voiceover was not created: the script is empty."

    try:
        from gtts import gTTS  # type: ignore

        tts = gTTS(
            text=text,
            lang="hi",
            slow=False
        )
        tts.save(str(destination))  # type: ignore
        return None
    except Exception as exc:
        return (
            f"Voiceover was not created: {type(exc).__name__}: {exc}. "
            "Check your internet connection and try again."
        )