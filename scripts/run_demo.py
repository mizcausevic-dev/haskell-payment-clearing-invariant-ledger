import json
from pathlib import Path

from haskell_payment_clearing_invariant_ledger import build_summary


summary = build_summary(json.loads(Path("fixtures/clearing_lanes.json").read_text(encoding="utf-8")))
print(f"estate={summary.estate}")
print(f"score={summary.aggregate_score:g}")
print(f"escalation={summary.escalation_lanes}")
print(f"volume_at_risk={summary.volume_at_risk}")
print(f"recommendation={summary.primary_recommendation}")

