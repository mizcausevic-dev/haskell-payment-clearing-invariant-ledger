import json
from pathlib import Path

from haskell_payment_clearing_invariant_ledger import build_summary
from haskell_payment_clearing_invariant_ledger.site import render_site


payload = json.loads(Path("fixtures/clearing_lanes.json").read_text(encoding="utf-8"))
Path("site").mkdir(exist_ok=True)
Path("site/index.html").write_text(render_site(build_summary(payload)), encoding="utf-8")

