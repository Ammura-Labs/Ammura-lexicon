import unittest

from processors.pronunciation import apply_pronunciations, parse_custom_dictionary
from processors.subtitles import generate_subtitles
from processors.notes import generate_notes


class ProcessorTests(unittest.TestCase):
    def test_custom_dictionary_overrides_default(self):
        result, changes = apply_pronunciations("Git and WiFi", {"Git": "gitt"})
        self.assertIn("gitt", result)
        self.assertIn("Wi-Fye", result)
        self.assertEqual(changes[0]["from"], "WiFi")

    def test_dictionary_parser_discards_invalid_rows(self):
        self.assertEqual(parse_custom_dictionary("A = B\ninvalid\n = none"), {"A": "B"})

    def test_subtitle_structure(self):
        subtitles = generate_subtitles("One two three four five six seven eight nine ten eleven twelve.")
        self.assertIn("00:00:00,000 -->", subtitles)
        self.assertIn("\n\n2\n", subtitles)

    def test_notes_are_bulleted(self):
        notes = generate_notes("This is one complete useful sentence. This is a second complete useful sentence.")
        self.assertTrue(notes.startswith("•"))


if __name__ == "__main__":
    unittest.main()
