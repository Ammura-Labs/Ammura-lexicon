# PRD: YouTube Video Scripting & AI Voiceover Assistant

## 1. Overview
This application automates the workflow for YouTube creators who use AI voiceovers.  
Users upload a **master script**, and the app generates four outputs:
- Narrative script (optimized for AI voiceover with pronunciation fixes)
- Subtitle script (.srt or plain text)
- Blog post (expanded, SEO-friendly)
- Notes (summary/bullet points)

The app also solves the **pronunciation problem** in AI TTS engines (e.g., “WhatsApp” → “Whats-app”, “WiFi” → “Wi-Fye”, “Git” → “Git (Gee-eye-tee)”).

---

## 2. Goals
- Simplify content creation for YouTube creators.
- Ensure AI voiceovers pronounce technical/brand terms correctly.
- Provide multiple content formats from a single script.
- Deliver outputs in editable file formats (.txt, .srt, .md, .mp3).

---

## 3. Target Users
- YouTube creators using AI voiceovers.
- Educators creating video lectures.
- Podcasters and bloggers repurposing scripts.

---

## 4. Features

### Input
- Upload master script (text file or paste text).
- Optional: User dictionary for custom pronunciation fixes.

### Processing
- **Pronunciation Fixer**: Replace problematic words before TTS.
- **Narrative Script Generator**: Adjust tone for spoken delivery.
- **Subtitle Generator**: Create timed or plain subtitles.
- **Blog Generator**: Expand script into SEO-friendly blog.
- **Notes Generator**: Summarize into bullet points.

### Output
- Narrative script (`narrative.txt`)
- Subtitle script (`subtitles.srt`)
- Blog post (`blog.md`)
- Notes (`notes.txt`)
- Optional: Voiceover audio (`voiceover.mp3`)

---

## 5. Technical Stack
- **Language**: Python
- **Frameworks**: Flask (web app) or Tkinter/PyQt (desktop)
- **Libraries**:
  - Text Processing: `nltk`, `spacy`, `transformers`
  - TTS: `gTTS`, `pyttsx3`, or external APIs (ElevenLabs/OpenAI)
  - File Handling: `os`, `pathlib`
- **Storage**: Local file system (outputs folder)

---

## 6. User Flow
1. User uploads master script.
2. System applies pronunciation fixes.
3. Generates narrative, subtitles, blog, and notes.
4. Outputs saved in `/outputs` folder.
5. Optional: Generate voiceover audio.

---

## 7. Future Enhancements
- Custom pronunciation dictionary per user.
- AI-powered subtitle timing (sync with audio).
- Multi-language support.
- Direct YouTube upload integration.
- Cloud storage (Google Drive/OneDrive).

---

## 8. Success Metrics
- Reduced manual editing time for creators.
- Improved AI voiceover accuracy.
- Increased content repurposing efficiency.
- Positive user adoption and feedback.

---
