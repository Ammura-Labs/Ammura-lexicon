import shutil
import unittest

import app as lexicon


class GenerateRouteTests(unittest.TestCase):
    """The /generate route is where a pronunciation entry reaches the user."""

    def setUp(self):
        lexicon.app.config["TESTING"] = True
        self.client = lexicon.app.test_client()

    def tearDown(self):
        for job_dir in lexicon.GENERATED_DIR.iterdir():
            if job_dir.is_dir():
                shutil.rmtree(job_dir, ignore_errors=True)

    def _generate(self, **form):
        response = self.client.post("/generate", data=form)
        self.assertEqual(response.status_code, 302)
        job_id = response.headers["Location"].rsplit("/", 1)[-1]
        return lexicon.GENERATED_DIR / job_id

    def test_generate_applies_the_default_dictionary(self):
        job_dir = self._generate(script="Use GitHub and WiFi today.")
        narrative = (job_dir / "narrative.txt").read_text(encoding="utf-8")
        self.assertIn("Git Hub", narrative)
        self.assertIn("Wi-Fye", narrative)

    def test_generate_accepts_a_backslash_in_a_custom_entry(self):
        job_dir = self._generate(script="Path C here.", dictionary="C = C:\\path")
        changes = (job_dir / "pronunciation-changes.json").read_text(encoding="utf-8")
        self.assertIn(r"C:\\path", changes)


if __name__ == "__main__":
    unittest.main()
