# Creator Studio — Script & Voiceover Assistant

A local-first Flask application that turns a source script into a voiceover-ready narrative, timed SRT subtitles, a Markdown blog post, and concise notes. It includes default and custom pronunciation replacements, plus optional gTTS MP3 generation.

## Run locally

```powershell
cd C:\Users\Harsh\Documents\Codex\2026-07-31\her\outputs\yt_script_app
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`. Generated job files are stored beneath `generated/` with a unique ID. Audio generation needs an internet connection because gTTS is an external service; all text output is local and still works without it.

## Tests

```powershell
python -m unittest discover -s tests
```
