from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from .ledger import build_summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Score payment clearing invariant pressure.")
    parser.add_argument("fixture", type=Path)
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()
    summary = build_summary(json.loads(args.fixture.read_text(encoding="utf-8")))
    if args.format == "json":
        print(json.dumps(asdict(summary), indent=2))
        return
    print(f"estate={summary.estate}")
    print(f"score={summary.aggregate_score:g}")
    print(f"escalation={summary.escalation_lanes}")
    print(f"volume_at_risk={summary.volume_at_risk}")
    print(f"recommendation={summary.primary_recommendation}")


if __name__ == "__main__":
    main()

