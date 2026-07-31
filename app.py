from __future__ import annotations

import json
import os
import re
import uuid
from pathlib import Path

from flask import Flask, abort, flash, redirect, render_template, request, send_from_directory, url_for

from processors.blog import generate_blog
from processors.narrative import generate_narrative
from processors.notes import generate_notes
from processors.pronunciation import apply_pronunciations, parse_custom_dictionary
from processors.subtitles import generate_subtitles
from processors.voiceover import generate_voiceover

BASE_DIR = Path(__file__).resolve().parent
GENERATED_DIR = BASE_DIR / "generated"
ALLOWED_EXTENSIONS = {"txt", "md"}

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", "local-development-only-change-me")
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024
GENERATED_DIR.mkdir(exist_ok=True)


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def save_outputs(script: str, custom_dictionary: dict[str, str], wants_audio: bool) -> tuple[str, list[dict[str, str | int]]]:
    job_id = uuid.uuid4().hex[:12]
    job_dir = GENERATED_DIR / job_id
    job_dir.mkdir()
    corrected, replacements = apply_pronunciations(script, custom_dictionary)
    files = {
        "narrative.txt": generate_narrative(corrected),
        "subtitles.srt": generate_subtitles(corrected),
        "blog.md": generate_blog(corrected),
        "notes.txt": generate_notes(corrected),
        "pronunciation-changes.json": json.dumps(replacements, indent=2),
    }
    for filename, content in files.items():
        (job_dir / filename).write_text(content, encoding="utf-8")

    if wants_audio:
        error = generate_voiceover(corrected, job_dir / "voiceover.mp3")
        if error:
            (job_dir / "voiceover-status.txt").write_text(error, encoding="utf-8")

    return job_id, replacements


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    script = request.form.get("script", "").strip()
    upload = request.files.get("script_file")
    if upload and upload.filename:
        if not allowed_file(upload.filename):
            flash("Please upload a .txt or .md file.", "error")
            return redirect(url_for("index"))
        script = upload.read().decode("utf-8", errors="replace").strip()

    if not script:
        flash("Paste a script or upload a non-empty text file to continue.", "error")
        return redirect(url_for("index"))
    if len(script) > 100_000:
        flash("Please keep scripts below 100,000 characters.", "error")
        return redirect(url_for("index"))

    custom_dictionary = parse_custom_dictionary(request.form.get("dictionary", ""))
    job_id, _ = save_outputs(script, custom_dictionary, request.form.get("audio") == "on")
    return redirect(url_for("results", job_id=job_id))


@app.route("/results/<job_id>")
def results(job_id: str):
    if not re.fullmatch(r"[a-f0-9]{12}", job_id) or not (GENERATED_DIR / job_id).is_dir():
        abort(404)
    job_dir = GENERATED_DIR / job_id
    file_map = {
        "narrative": ("Narrative", "narrative.txt", "text"),
        "subtitles": ("Subtitles", "subtitles.srt", "text"),
        "blog": ("Blog", "blog.md", "markdown"),
        "notes": ("Notes", "notes.txt", "text"),
    }
    outputs: list[dict[str, str]] = []
    for key, (label, filename, kind) in file_map.items():
        outputs.append({"key": key, "label": label, "filename": filename, "kind": kind,
                        "content": (job_dir / filename).read_text(encoding="utf-8")})
    replacements = json.loads((job_dir / "pronunciation-changes.json").read_text(encoding="utf-8"))
    audio_ready = (job_dir / "voiceover.mp3").exists()
    audio_error = (job_dir / "voiceover-status.txt").read_text(encoding="utf-8") if (job_dir / "voiceover-status.txt").exists() else None
    return render_template("results.html", job_id=job_id, outputs=outputs, replacements=replacements,
                           audio_ready=audio_ready, audio_error=audio_error)


@app.route("/download/<job_id>/<filename>")
def download(job_id: str, filename: str):
    if not re.fullmatch(r"[a-f0-9]{12}", job_id) or filename not in {"narrative.txt", "subtitles.srt", "blog.md", "notes.txt", "voiceover.mp3"}:
        abort(404)
    return send_from_directory(GENERATED_DIR / job_id, filename, as_attachment=True)


@app.errorhandler(413)
def too_large(_error: Exception):
    flash("The uploaded file is too large. The limit is 2 MB.", "error")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
