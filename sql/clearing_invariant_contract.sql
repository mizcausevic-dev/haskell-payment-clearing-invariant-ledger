create view clearing_invariant_ledger as
select
  lane_id,
  rail,
  daily_volume,
  unmatched_debits,
  late_batches,
  liquidity_hold_percent,
  manual_override_count,
  reconciliation_delay_minutes,
  owner,
  next_action,
  case
    when unmatched_debits >= 30 or liquidity_hold_percent >= 10 then 'escalate'
    when unmatched_debits >= 10 or liquidity_hold_percent >= 5 then 'watch'
    else 'contained'
  end as clearing_posture
from reviewed_payment_clearing_lanes;

