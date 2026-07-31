# Rules: YouTube Video Scripting & AI Voiceover Assistant

## 1. General Guidelines
- Keep the app **modular**: separate processors for narrative, subtitles, blog, notes, and pronunciation.
- Ensure outputs are **editable text files** (`.txt`, `.srt`, `.md`) and optional audio (`.mp3`).
- Maintain **clarity and consistency** across generated outputs.
- Prioritize **local execution** first; external APIs optional for advanced features.

---

## 2. What to Use
- **Python 3.10+**
- **Frameworks**:
  - Flask (for web app) or Tkinter/PyQt (for desktop UI)
- **Libraries**:
  - Text Processing: `nltk`, `spacy`, `transformers`
  - Summarization/Expansion: Hugging Face models (`transformers`)
  - TTS: `gTTS`, `pyttsx3` (local), optional APIs (ElevenLabs, OpenAI TTS)
  - File Handling: `os`, `pathlib`
- **Storage**: Local file system (`outputs/` folder)

---

## 3. What to Avoid
- Avoid **hardcoding outputs**; always generate dynamically.
- Avoid **ambiguous AI prompts** (be explicit in instructions to models).
- Avoid **over-reliance on external APIs** (ensure local fallback).
- Avoid **mixing UI and logic**; keep processors separate from frontend.
- Avoid **blocking operations** in Flask/Tkinter; use async/threading if needed.

---

## 4. Error Handling
- **Input Validation**:
  - Check if uploaded script is non-empty.
  - Validate file types (`.txt`, `.md`).
- **Pronunciation Fixer**:
  - If word not found in dictionary, leave unchanged.
- **AI Model Failures**:
  - Fallback to simpler text processing (e.g., `nltk` summarizer).
- **TTS Failures**:
  - Provide text output even if audio generation fails.
- **File Handling**:
  - Ensure outputs are saved in `/outputs` with unique filenames.
  - Catch `IOError` and notify user.

---

## 5. Boundaries for AI
- AI should **not invent facts**; only transform or expand user-provided script.
- AI should **not alter meaning** of master script; only adjust for format or pronunciation.
- AI should **not generate offensive or harmful content**.
- AI should **not override user’s custom dictionary**; user-defined corrections take priority.
- AI should **not produce copyrighted material verbatim**; only generate derivative outputs.

---

## 6. Output Standards
- **Narrative Script**: Conversational, voiceover-friendly.
- **Subtitle Script**: Plain `.srt` format or text with timestamps (future enhancement).
- **Blog Post**: Expanded, SEO-friendly, markdown format.
- **Notes**: Bullet-point summary, concise.

---

## 7. Future-Proofing
- Allow **custom pronunciation dictionary per user**.
- Add **multi-language support**.
- Integrate **cloud storage** for outputs.
- Enable **direct YouTube upload** (future API integration).
