from pathlib import Path

source = Path("haskell/ClearingInvariant.hs").read_text(encoding="utf-8")
required = ["module ClearingInvariant", "data ClearingLane", "invariantPasses", "explainInvariant", "debitsEqualCredits"]
missing = [token for token in required if token not in source]
if missing:
    raise SystemExit(f"missing Haskell invariant token(s): {', '.join(missing)}")
print("haskell contract ok")

