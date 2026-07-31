# Phases: YouTube Video Scripting & AI Voiceover Assistant

## Phase 1: Planning & Setup
- Define scope and outputs (Narrative, Subtitles, Blog, Notes).
- Create initial project structure (`yt_script_app/`).
- Draft PRD, Architecture, and Rules documents.
- Prepare `requirements.txt` with essential libraries.

---

## Phase 2: Core Processing Modules
- **Pronunciation Fixer**:
  - Build dictionary for common mispronunciations.
  - Implement replacement logic.
- **Narrative Generator**:
  - Adjust master script for spoken delivery.
- **Subtitle Generator**:
  - Generate plain text subtitles (timed version later).
- **Blog Generator**:
  - Expand script into SEO-friendly markdown.
- **Notes Generator**:
  - Summarize into concise bullet points.

---

## Phase 3: Integration & Workflow
- Connect all processors in `app.py`.
- Ensure outputs are saved in `/outputs` folder.
- Add error handling for empty scripts, invalid files, and failed processing.
- Test with sample scripts.

---

## Phase 4: Voiceover (TTS)
- Integrate basic TTS (`gTTS`, `pyttsx3`).
- Apply pronunciation fixes before TTS.
- Save audio as `voiceover.mp3`.

---

## Phase 5: User Interface
- **Option A (Web)**: Flask app with upload form and download links.
- **Option B (Desktop)**: Tkinter/PyQt app with file upload and buttons.
- Provide clear feedback messages (success, errors).

---

## Phase 6: Enhancements
- Custom pronunciation dictionary per user.
- Subtitle timing synced with audio.
- Multi-language support.
- Cloud storage integration (Google Drive/OneDrive).
- Direct YouTube upload API.

---

## Phase 7: Testing & Deployment
- Unit tests for each processor.
- End-to-end testing with sample scripts.
- Package app for distribution.
- Deploy web version (Heroku/Render) or desktop installer.

---

## Phase 8: Future Roadmap
- Collaboration features (shared dictionaries).
- AI-powered editing suggestions.
- Integration with video editing tools.
