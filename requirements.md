# Requirements: YouTube Video Scripting & AI Voiceover Assistant

## 1. System Requirements
- **Python**: 3.10+
- **OS**: Windows, macOS, Linux
- **Storage**: Local file system for outputs
- **Optional**: Internet connection for external APIs (TTS, Hugging Face)

---

## 2. Python Dependencies
- **Web Framework**
  - Flask (for web app) OR Tkinter/PyQt (for desktop)
- **Text Processing**
  - nltk
  - spacy
  - transformers (Hugging Face)
- **TTS**
  - gTTS
  - pyttsx3
- **Utilities**
  - pathlib
  - os
  - rich (for CLI feedback, optional)

---

## 3. Functional Requirements
- Upload master script (text file or paste).
- Apply pronunciation fixes.
- Generate:
  - Narrative script (`narrative.txt`)
  - Subtitle script (`subtitles.srt`)
  - Blog post (`blog.md`)
  - Notes (`notes.txt`)
- Optional: Generate voiceover audio (`voiceover.mp3`).
- Save all outputs in `/outputs` folder.
- Provide download links via UI.

---

## 4. Non-Functional Requirements
- **Performance**: Process scripts under 5 seconds for <5k words.
- **Scalability**: Support larger scripts with streaming output.
- **Usability**: Simple, intuitive UI with clear feedback.
- **Reliability**: Fallbacks for AI failures (basic summarization).
- **Security**: Sanitize user input, prevent code injection.

---

## 5. Future Requirements
- Custom pronunciation dictionary per user.
- Subtitle timing synced with audio.
- Multi-language support.
- Cloud storage integration.
- Direct YouTube upload API.
