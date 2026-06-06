from pathlib import Path

sql = Path("sql/clearing_invariant_contract.sql").read_text(encoding="utf-8").lower()
required = ["create view", "clearing_invariant_ledger", "unmatched_debits", "liquidity_hold_percent", "reconciliation_delay_minutes"]
missing = [token for token in required if token not in sql]
if missing:
    raise SystemExit(f"missing sql contract token(s): {', '.join(missing)}")
print("sql contract ok")

