import json
import unittest
from pathlib import Path

from haskell_payment_clearing_invariant_ledger import build_summary, score_lane


FIXTURE = json.loads(Path("fixtures/clearing_lanes.json").read_text(encoding="utf-8"))


class ClearingInvariantLedgerTests(unittest.TestCase):
    def test_prioritizes_same_day_ach(self) -> None:
        summary = build_summary(FIXTURE)
        self.assertEqual(summary.escalation_lanes, 2)
        self.assertEqual(summary.findings[0].lane_id, "same-day-ach-window")
        self.assertEqual(summary.volume_at_risk, 4482900)
        self.assertIn("debit-credit parity", summary.primary_recommendation)

    def test_wire_lane_is_contained(self) -> None:
        finding = score_lane(FIXTURE["lanes"][2])
        self.assertEqual(finding.posture, "contained")
        self.assertLess(finding.score, 45)

    def test_requires_lane(self) -> None:
        with self.assertRaisesRegex(ValueError, "At least one clearing invariant lane is required."):
            build_summary({"lanes": []})


if __name__ == "__main__":
    unittest.main()
