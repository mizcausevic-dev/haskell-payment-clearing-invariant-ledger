from pathlib import Path

html = Path("site/index.html").read_text(encoding="utf-8")
required = [
    "Haskell Payment Clearing Invariant Ledger",
    "Settlement exceptions stay provable",
    "same-day-ach-window",
    "card-clearing-adjustments",
]
missing = [token for token in required if token not in html]
if missing:
    raise SystemExit(f"missing site marker(s): {', '.join(missing)}")
print("smoke ok")

