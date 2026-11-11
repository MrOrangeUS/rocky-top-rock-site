"""Offline regression checks for the site's first-party font delivery."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class FontPrivacyTests(unittest.TestCase):
    def test_no_remote_font_references(self):
        forbidden = ("fonts." + "googleapis.com", "fonts." + "gstatic.com")
        files = [*ROOT.glob("*.html"), *ROOT.rglob("*.css"), *ROOT.rglob("*.js")]
        for path in files:
            with self.subTest(path=path.relative_to(ROOT)):
                content = path.read_text(encoding="utf-8").lower()
                self.assertFalse(any(host in content for host in forbidden))

    def test_every_page_uses_local_fonts(self):
        pages = list(ROOT.glob("*.html"))
        self.assertEqual(len(pages), 6)
        for path in pages:
            with self.subTest(page=path.name):
                self.assertIn('href="assets/fonts/montserrat.css"', path.read_text(encoding="utf-8"))

    def test_font_files_are_local_valid_woff2(self):
        css = (ROOT / "assets/fonts/montserrat.css").read_text(encoding="utf-8")
        urls = re.findall(r"url\(([^)]+)\)", css)
        self.assertEqual(len(set(urls)), 5)
        for url in urls:
            with self.subTest(url=url):
                self.assertTrue(url.startswith("./"))
                self.assertNotIn("..", url)
                data = (ROOT / "assets/fonts" / url).read_bytes()
                self.assertEqual(data[:4], b"wOF2")
                self.assertGreater(len(data), 1000)
                self.assertEqual(int.from_bytes(data[8:12], "big"), len(data))

    def test_original_weights_subsets_and_license(self):
        css = (ROOT / "assets/fonts/montserrat.css").read_text(encoding="utf-8")
        self.assertEqual(css.count("@font-face"), 20)
        for weight in (400, 500, 600, 700):
            self.assertEqual(css.count(f"font-weight: {weight};"), 5)
        for subset in ("latin", "latin-ext", "vietnamese", "cyrillic", "cyrillic-ext"):
            self.assertEqual(css.count(f"/* {subset} */"), 4)
        self.assertEqual(css.count("font-display: swap;"), 20)
        self.assertIn("SIL OPEN FONT LICENSE Version 1.1", (ROOT / "assets/fonts/OFL.txt").read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()