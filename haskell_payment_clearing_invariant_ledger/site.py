from __future__ import annotations

import html

from .ledger import ClearingSummary


def render_site(summary: ClearingSummary) -> str:
    cards = "\n".join(
        f"""<article class="lane {finding.posture}">
<span>{html.escape(finding.posture)}</span>
<h3>{html.escape(finding.lane_id)}</h3>
<p>{html.escape(finding.rail)} resolves into a {finding.score:g} invariant score with ${finding.volume_at_risk:,} of daily volume under hold pressure.</p>
<dl><div><dt>Owner</dt><dd>{html.escape(finding.owner)}</dd></div><div><dt>Score</dt><dd>{finding.score:g}</dd></div></dl>
<strong>{html.escape(finding.next_action)}</strong>
</article>"""
        for finding in summary.findings
    )
    depth_cards = """<article class="depth-card story">
<span>SaaS go-to-market analyst lens</span>
<h3>Turns payment-clearing exceptions into a trust and liquidity story.</h3>
<p>Settlement failures are not just back-office defects. Unmatched debits, late batches, reconciliation delay, and manual overrides can become customer trust, partner confidence, regulatory, and investor-readiness problems if leadership sees them too late.</p>
</article>
<article class="depth-card">
<span>SaaS value architect lens</span>
<h3>Connects invariant breaks to volume at risk and remediation priority.</h3>
<p>The ledger shows which payment rails have the highest clearing exposure, who owns the lane, and what action reduces avoidable liquidity hold pressure. It helps finance, product, risk, and engineering align on the next intervention.</p>
</article>
<article class="depth-card">
<span>Technical proof</span>
<h3>The repo makes the invariant contract inspectable.</h3>
<p>It includes a Python scoring model, a Haskell invariant contract, SQL evidence checks, synthetic clearing fixtures, CLI output, unit tests, smoke checks, generated screenshots, and a static executive surface.</p>
</article>
<article class="depth-card">
<span>What these repos have in common</span>
<h3>They convert operational exceptions into defensible decision surfaces.</h3>
<p>The shared Kinetic Gain pattern is to expose the risk lane, preserve traceable evidence, score priority, assign ownership, and publish a readable surface for leaders without hiding the underlying technical contract.</p>
</article>"""
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/><title>Haskell Payment Clearing Invariant Ledger</title><meta name="description" content="Haskell payment clearing invariant ledger for settlement exceptions, liquidity holds, unmatched debits, and operator-safe proof."/><style>
:root{{--bg:#050812;--panel:#0d1727;--text:#f4f1ea;--muted:#a8b3c7;--cyan:#25d7ef;--green:#58f0b3;--pink:#ff72b6;--line:rgba(37,215,239,.24)}}*{{box-sizing:border-box}}body{{margin:0;font-family:"Segoe UI",sans-serif;color:var(--text);background:radial-gradient(circle at 82% 6%,rgba(88,240,179,.12),transparent 34rem),radial-gradient(circle at 12% 10%,rgba(37,215,239,.13),transparent 30rem),var(--bg)}}main{{width:min(1180px,calc(100% - 40px));margin:0 auto;padding:56px 0}}.hero,.section-panel{{background:linear-gradient(135deg,rgba(13,23,39,.96),rgba(8,11,24,.92));border:1px solid var(--line);border-radius:28px}}.hero{{padding:clamp(30px,5vw,64px)}}.section-panel{{margin-top:26px;padding:28px}}.kicker,.note{{color:var(--green);font-family:Consolas,monospace;font-size:.78rem;letter-spacing:.18em;text-transform:uppercase}}h1{{max-width:1040px;margin:18px 0;font-size:clamp(3rem,7.2vw,6.2rem);line-height:.92;letter-spacing:-.075em}}.lede{{max-width:790px;color:var(--muted);font-size:1.24rem;line-height:1.7}}.metrics,.grid,.depth-grid{{display:grid;gap:16px}}.metrics{{grid-template-columns:repeat(4,1fr);margin-top:34px}}.metric,.lane,.depth-card{{background:rgba(13,23,39,.9);border:1px solid rgba(255,255,255,.08);border-radius:20px;padding:22px}}.metric small,dt{{color:var(--muted);text-transform:uppercase;letter-spacing:.12em;font-size:.75rem}}.metric b{{display:block;margin-top:10px;font-size:2rem}}.section-head{{display:flex;align-items:end;justify-content:space-between;gap:16px;margin-bottom:16px;border-bottom:1px solid rgba(255,255,255,.08);padding-bottom:14px}}.section-head h2{{font-size:clamp(2rem,4vw,3.4rem);line-height:.95;letter-spacing:-.05em;margin:0}}.note{{color:var(--muted)}}.depth-grid{{grid-template-columns:repeat(4,1fr)}}.grid{{grid-template-columns:repeat(3,1fr);margin-top:22px}}.lane,.depth-card{{min-height:330px}}.lane span,.depth-card span{{color:var(--cyan);font-family:Consolas,monospace;text-transform:uppercase;letter-spacing:.14em;font-size:.76rem}}.depth-card.story{{border-left:4px solid var(--cyan)}}.lane.escalate{{border-color:rgba(255,114,182,.5)}}.lane.watch{{border-color:rgba(157,140,255,.44)}}.lane.contained{{border-color:rgba(88,240,179,.45)}}h3{{font-size:1.45rem;margin:14px 0 10px}}p{{color:var(--muted);line-height:1.6}}dl{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:20px 0}}dd{{margin:5px 0 0;font-size:1.1rem;font-weight:800}}footer{{margin-top:34px;color:var(--muted);font-family:Consolas,monospace}}@media(max-width:1100px){{.depth-grid{{grid-template-columns:repeat(2,1fr)}}}}@media(max-width:900px){{.metrics,.grid,.depth-grid,dl{{grid-template-columns:1fr}}.section-head{{align-items:flex-start;flex-direction:column}}}}
</style></head><body><main><section class="hero"><div class="kicker">Haskell / Payments / Clearing Invariants</div><h1>Settlement exceptions stay provable before liquidity risk becomes a board surprise.</h1><p class="lede">Haskell Payment Clearing Invariant Ledger turns unmatched debits, late batches, liquidity holds, manual overrides, and reconciliation delay into one executive-ready clearing proof.</p><div class="metrics"><div class="metric"><small>Aggregate score</small><b>{summary.aggregate_score:g}</b></div><div class="metric"><small>Escalation lanes</small><b>{summary.escalation_lanes}</b></div><div class="metric"><small>Volume at risk</small><b>${summary.volume_at_risk:,}</b></div><div class="metric"><small>Top lane</small><b>{html.escape(summary.findings[0].lane_id)}</b></div></div></section><section class="section-panel"><div class="section-head"><h2>What this product does</h2><div class="note">clearing risk / liquidity proof / settlement trust</div></div><div class="depth-grid">{depth_cards}</div></section><section class="section-panel"><div class="section-head"><h2>Clearing lanes</h2><div class="note">rails / holds / invariant checks</div></div><div class="grid">{cards}</div></section><footer>Primary recommendation: {html.escape(summary.primary_recommendation)}</footer></main></body></html>"""
