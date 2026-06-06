from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ClearingFinding:
    lane_id: str
    rail: str
    score: float
    posture: str
    volume_at_risk: int
    owner: str
    next_action: str


@dataclass(frozen=True)
class ClearingSummary:
    estate: str
    aggregate_score: float
    escalation_lanes: int
    volume_at_risk: int
    primary_recommendation: str
    findings: list[ClearingFinding]


def _num(lane: dict[str, Any], key: str) -> float:
    try:
        return float(lane[key])
    except KeyError as exc:
        raise ValueError(f"Missing required lane field: {key}") from exc


def score_lane(lane: dict[str, Any]) -> ClearingFinding:
    unmatched = min(_num(lane, "unmatched_debits"), 50) * 1.45
    late = _num(lane, "late_batches") * 5.2
    hold = _num(lane, "liquidity_hold_percent") * 2.4
    overrides = _num(lane, "manual_override_count") * 2.1
    delay = min(_num(lane, "reconciliation_delay_minutes"), 180) * 0.18
    score = round(min(100.0, unmatched + late + hold + overrides + delay), 2)
    posture = "escalate" if score >= 70 else "watch" if score >= 45 else "contained"
    volume_at_risk = int(round(_num(lane, "daily_volume") * (_num(lane, "liquidity_hold_percent") / 100)))
    return ClearingFinding(
        lane_id=str(lane["lane_id"]),
        rail=str(lane["rail"]),
        score=score,
        posture=posture,
        volume_at_risk=volume_at_risk,
        owner=str(lane["owner"]),
        next_action=str(lane["next_action"]),
    )


def build_summary(payload: dict[str, Any]) -> ClearingSummary:
    lanes = payload.get("lanes") or []
    if not lanes:
        raise ValueError("At least one clearing invariant lane is required.")
    findings = sorted((score_lane(lane) for lane in lanes), key=lambda item: item.score, reverse=True)
    aggregate = round(sum(item.score for item in findings) / len(findings), 2)
    escalation_lanes = sum(1 for item in findings if item.posture == "escalate")
    volume_at_risk = sum(item.volume_at_risk for item in findings)
    return ClearingSummary(
        estate=str(payload.get("estate", "Payment clearing invariant estate")),
        aggregate_score=aggregate,
        escalation_lanes=escalation_lanes,
        volume_at_risk=volume_at_risk,
        primary_recommendation=f"{findings[0].lane_id}: {findings[0].next_action}",
        findings=findings,
    )

