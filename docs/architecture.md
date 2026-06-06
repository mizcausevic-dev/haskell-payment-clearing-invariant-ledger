# Architecture

This repo is a synthetic payment-clearing proof surface. It does not connect to payment processors, banks, card networks, or production ledgers.

## Layers

- `fixtures/clearing_lanes.json` provides synthetic reviewed clearing lanes.
- `haskell/ClearingInvariant.hs` documents the invariant shape in Haskell.
- `haskell_payment_clearing_invariant_ledger/ledger.py` scores operator posture.
- `sql/clearing_invariant_contract.sql` names the reviewed fields expected from a warehouse view.
- `scripts/prerender.py` writes the static GitHub Pages artifact.

## Safety boundary

No credentials, account numbers, card data, payment tokens, customer records, or processor exports belong in this repository.

