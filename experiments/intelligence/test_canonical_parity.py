"""Parity checks against checked-in canonical method, not duplicate ownership."""
import re
import unittest
from pathlib import Path

from intelligence.vocabulary import SOURCE_OUTCOMES, RESEARCH_STATUSES, RESEARCH_REQUIRED

ROOT = Path(__file__).resolve().parents[2]
RESEARCH = ROOT / "src/ai-creative-skill/references/AI_Creative_Skill_Method_Research_Evidence_Synthesis_Pre-v0.3.md"


class CanonicalParity(unittest.TestCase):
    def test_exact_source_outcome_vocabulary_from_owner_method(self):
        text = RESEARCH.read_text(encoding="utf-8")
        section = text.split("# 6. Source Outcome and Coverage Discipline", 1)[1]
        block = section.split("```text", 1)[1].split("```", 1)[0]
        values = set(x.strip() for x in block.splitlines() if x.strip())
        self.assertEqual(values, set(SOURCE_OUTCOMES))

    def test_canonical_research_status_vocabulary(self):
        text = RESEARCH.read_text(encoding="utf-8")
        section = text.split("# 14. Output", 1)[1]
        self.assertIn("COMPLETE | PARTIAL | INSUFFICIENT_EVIDENCE | BLOCKED", section)
        self.assertEqual(4, len(RESEARCH_STATUSES))

    def test_required_envelope_fields_reference_existing_method(self):
        text = RESEARCH.read_text(encoding="utf-8")
        section = text.split("# 14. Output", 1)[1].split("```yaml", 1)[1].split("```", 1)[0]
        for key in RESEARCH_REQUIRED:
            with self.subTest(field=key):
                self.assertIn(key + ":", section)


if __name__ == "__main__":
    unittest.main()
