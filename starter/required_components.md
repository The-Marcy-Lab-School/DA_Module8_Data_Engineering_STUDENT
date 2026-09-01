# Required Components

Every one of these must be real and demonstrated — not asserted. Fill in
what you actually built/found for each section; this is graded alongside
the pipeline itself.

## 1. The pipeline (extract → transform → load)

**Your team's real external sources — both, and who owned each path**
(per `team_charter.md`): TODO

**Which approach your pipeline uses — ETL or ELT — and why** (tie it to
your real source/target and actual data volume/latency, not a generic
answer): TODO

**Your target tables, in your team's chosen Module 3/8 warehouse** (one
per source): TODO

**Real row counts from an actual triggered run** (query both target
tables directly, paste the real results): TODO

## 2. Failure handling — a real test, not a configured-and-assumed one

The single most common failure on this section: retries configured but
never actually tested. Don't let that be you.

**How you broke the source on purpose** (a real, specific action — rename
a column, kill the connection mid-run, point at a bad URL): TODO

**What actually happened** — paste the real task log/error, and confirm
whether the retry actually fired and whether it recovered or correctly
failed after exhausting retries: TODO

## 3. Monitoring & alerting

**Where structured logs are emitted, and what they actually say** (paste
a real log line per task, not a description of what you'd expect to
see): TODO

**Your real alert, and how you confirmed it actually fires on failure**
(not just configured): TODO

## 4. The CI gap

**What was actually missing from the given `.github/workflows/ci.yml`,**
and why it matters (what could pass the old CI and still be broken)?
TODO

**Your fix, and proof it works**: trigger a PR with a deliberately broken
DAG, paste the real CI failure output, then fix it and paste the real
CI success output. Two real runs, not one assumed.

## 5. Project management

**Link to `backlog.md` and `team_charter.md`** — both should already
exist and be filled in from before you started building, not backfilled
now.

## 6. Git collaboration (a real team, not a pair)

**Every feature branch that was merged, and who reviewed each one** —
list them, not just the last one: TODO

**≥2 real, substantive review comments given to teammates** (paste them
— "LGTM" doesn't count), and who gave which: TODO

**≥2 real peer comments received and incorporated**, and what changed in
response: TODO

**Confirm branch protection was actually on `main`** (a screenshot or a
description of the settings) — this is what makes the review requirement
real, not optional: TODO

**Your milestone check-in** — see `backlog.md`'s own section for this;
confirm here that it was reported proactively, not after being asked.

## 7. Team accountability

**Link to `team_charter.md`** (the filled-in RACI) and every team
member's own `individual_reflection_<name>.md`.

**The group readout** — who presented which piece, and a one-line note
on how the Q&A for each piece actually went (a role that couldn't
answer a question about its own area is worth noting honestly here).
