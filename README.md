# haskell-payment-clearing-invariant-ledger

[![ci](https://github.com/mizcausevic-dev/haskell-payment-clearing-invariant-ledger/actions/workflows/ci.yml/badge.svg)](https://github.com/mizcausevic-dev/haskell-payment-clearing-invariant-ledger/actions/workflows/ci.yml)
[![pages](https://github.com/mizcausevic-dev/haskell-payment-clearing-invariant-ledger/actions/workflows/pages.yml/badge.svg)](https://github.com/mizcausevic-dev/haskell-payment-clearing-invariant-ledger/actions/workflows/pages.yml)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](LICENSE)

Haskell Payment Clearing Invariant Ledger turns unmatched debits, late batches, liquidity holds, manual overrides, and reconciliation delay into one executive-ready clearing proof.

## Why this exists

- Payment risk gets vague when settlement exceptions, holds, overrides, and parity checks live in separate operating reviews.
- Haskell is a high-signal language for invariant-heavy financial systems, even when the public surface is Python and SQL friendly.
- The repo gives practical FinTech / clearing / Haskell proof without using production payment data or credentials.

## Screenshots

![Overview proof](screenshots/01-overview-proof.png)

![Invariant proof](screenshots/02-ledger-proof.png)

## What it includes

- Python scoring model and CLI.
- Haskell invariant contract.
- SQL evidence contract for reviewed clearing fields.
- Static GitHub Pages executive surface.
- Synthetic payment-clearing fixture data.
- CI, Pages deploy, smoke checks, screenshots, docs, and security notes.

## Local run

```bash
python -m pip install -e .
python -m unittest discover -s tests
python scripts/run_demo.py
python scripts/check_sql.py
python scripts/check_haskell_contract.py
python scripts/prerender.py
python scripts/smoke_check.py
```

## CLI

```bash
haskell-payment-clearing-invariant-ledger fixtures/clearing_lanes.json
haskell-payment-clearing-invariant-ledger fixtures/clearing_lanes.json --format json
```

## Board question answered

> Which clearing lanes threaten settlement proof, liquidity posture, and payment-risk narrative before the next board or investor review?

