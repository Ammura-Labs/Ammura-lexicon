# Architecture: YouTube Video Scripting & AI Voiceover Assistant

## 1. App Flow

### Step 1: Input
- User uploads or pastes a **master script**.
- Optional: User provides a custom pronunciation dictionary.

### Step 2: Preprocessing
- **Pronunciation Fixer** replaces problematic words (e.g., WhatsApp → Whats-app).
- Cleaned text is passed to downstream processors.

### Step 3: Processing Modules
- **Narrative Generator**: Adjusts script for spoken delivery.
- **Subtitle Generator**: Produces `.srt` or plain text subtitles.
- **Blog Generator**: Expands script into SEO-friendly blog format.
- **Notes Generator**: Summarizes into bullet points.

### Step 4: Output
- Narrative script → `outputs/narrative.txt`
- Subtitle script → `outputs/subtitles.srt`
- Blog post → `outputs/blog.md`
- Notes → `outputs/notes.txt`
- Optional voiceover audio → `outputs/voiceover.mp3`

### Step 5: Delivery
- Files available for download via web UI or saved locally.

---

## 2. Architecture Diagram (Conceptual)

┌───────────────┐
│   Master      │
│   Script      │
└───────┬───────┘
│
┌───────▼────────┐
│ Pronunciation  │
│ Fixer          │
└───────┬────────┘
│
┌──────────────┼─────────────────────────┐
│              │                         │
┌──▼───┐     ┌────▼────┐              ┌─────▼─────┐
│Narr- │     │Subtitle │              │Blog       │
│ative │     │Generator│              │Generator  │
│Gen.  │     └────┬────┘              └─────┬─────┘
└──┬───┘          │                        │
│              │                        │
│         ┌────▼────┐                   │
│         │Notes    │                   │
│         │Generator│                   │
│         └────┬────┘                   │
│              │                        │
└──────────────┼────────────────────────┘
│
┌───────▼────────┐
│   Outputs      │
│ (txt, srt, md, │
│  mp3)          │
└────────────────┘


---

## 3. File & Folder Structure

yt_script_app/
│── app.py                # Main Flask/Tkinter app
│── processors/
│   ├── narrative.py       # Voiceover-friendly script generator
│   ├── subtitles.py       # Subtitle generator
│   ├── blog.py            # Blog expansion
│   ├── notes.py           # Notes summarizer
│   └── pronunciation.py   # Word correction logic
│── outputs/               # Generated files
│── templates/             # HTML templates (Flask UI)
│── static/                # CSS/JS assets (Flask UI)
│── requirements.txt       # Python dependencies
│── prd.md                 # Product Requirements Document
│── architecture.md        # Architecture & App Flow
│── rules.md               # what to use and avoid
│── design.md              # design of app
│── phases.md              #phases to design
│── wireframe.md

---

## 4. Tech Stack

### Backend
- **Language**: Python
- **Frameworks**: Flask (web app) or Tkinter/PyQt (desktop)
- **Libraries**:
  - Text Processing: `nltk`, `spacy`, `transformers`
  - Summarization/Expansion: Hugging Face models
  - TTS: `gTTS`, `pyttsx3`, or external APIs (ElevenLabs/OpenAI)
  - File Handling: `os`, `pathlib`

### Frontend
- **Web UI**: HTML, CSS, JS (served via Flask)
- **Desktop UI (optional)**: Tkinter/PyQt

### Storage
- Local file system (`outputs/` folder)
- Optional cloud integration (Google Drive/OneDrive)

---

## 5. Scalability & Future Enhancements
- Add **custom pronunciation dictionary per user**.
- Integrate **AI-powered subtitle timing** synced with audio.
- Support **multi-language scripts**.
- Enable **direct YouTube upload**.
- Cloud storage and collaboration features.

---
