# MVP — the real bar for "done"

This is what actually gets graded as Meets/Approaching/Below per skill.
See instructor `rubric.md` for the full rubric if your instructor has
shared it — this is the same bar in checklist form.

## The pipeline

- [ ] A real Airflow DAG, on a real schedule (`@daily`/`@hourly`), that
      runs end-to-end with **no manual intervention** once triggered.
- [ ] Extract from **both** real external sources (`SCENARIOS.md`) —
      Open-Meteo and NASA, each with its own owner (per
      `team_charter.md`); transform in real Python tasks; load into two
      **new tables** in your team's chosen Module 3/8 warehouse — real
      row counts land, confirmed with a direct `SELECT`, not just "the
      task turned green."
- [ ] Correctly identifies (and can explain) whether your specific
      source/target justifies an ETL or ELT approach — not just the
      textbook definitions.
- [ ] Task dependencies correctly ordered; retries configured with a
      real, reasoned strategy.

## Failure handling — genuinely tested, not just configured

- [ ] Retries **genuinely tested** against a real simulated failure (a
      renamed column, a killed connection, a bad URL) — not just
      configured and assumed to work. This is `common_project_mistakes`'
      #1 failure mode; don't let it be yours.
- [ ] Structured logs at every task.
- [ ] At least one real alert, **confirmed to actually fire** on a real
      task failure (not assumed to work because it's configured).

## CI

- [ ] The real gap in `starter/.github/workflows/ci.yml` found and named
      (`required_components.md` Section 4).
- [ ] Fixed — and the fix proven: a run that fails on a deliberately
      broken test/lint issue, and a run that passes once it's fixed
      (two real runs, not one).

## Project management & team accountability

- [ ] `team_charter.md` written **before** any real DAG logic — a real
      RACI naming one clear accountable owner per real task, not
      everyone marked the same on every row.
- [ ] `backlog.md` written **before** any real DAG logic — ≥5 discrete,
      sequenced, **owned** tasks with real estimated durations.
- [ ] Task order in the backlog is **justified against the real
      deadline and dependency chain** — not just listed arbitrarily
      (e.g., "build extract task" genuinely precedes "write monitoring
      alerts" because monitoring needs something to monitor).
- [ ] A real, proactive milestone check-in (on track / at risk, with a
      specific reason if at risk) — reported before being asked, not
      backfilled at the end.
- [ ] Each member's own `individual_reflection_<name>.md`, with real,
      checkable evidence (commit/PR links) for their own RACI row.

## Git & collaboration

- [ ] Shared `.gitignore`/`LICENSE`, written from scratch by the team —
      real work always happens on a feature branch, never directly on
      `main`, enforced by real **branch protection** (≥1 approving
      review required).
- [ ] ≥2 real, substantive review comments given, by ≥2 different team
      members, and ≥2 real peer comments received and visibly
      incorporated into the merged code. Pull requests are merged only
      after real review — not a single self-approved commit with no
      peer comment.

## The group readout

- [ ] Each role presents their own piece (PM: scope/timeline, Tech Lead:
      architecture, Business Analyst: what the pipeline serves and why,
      QA/Reliability Lead: failure-handling/monitoring) and fields real
      Q&A on it.

## Written work

- [ ] `starter/required_components.md` — all 7 sections filled in for
      real, as you go (not from memory at the end): both real pipelines
      and their real row counts, the real break-it-on-purpose test and
      what actually happened, the real monitoring/alert evidence, the
      real CI gap and its fix, the backlog/charter links, the real team
      PR record, and the team-accountability evidence.

## What "Below" looks like, concretely

- Retries configured but never actually tested against a real failure.
- Only one of the two required sources genuinely built.
- The backlog/charter written retroactively, after the pipeline already
  works, instead of before starting the build.
- A RACI where every role is marked the same on every row — diffused,
  not real, accountability.
- A pull request that's a single self-approved commit with no real peer
  review, or branch protection never actually turned on.
- No alerting configured, so a failed run would go unnoticed until
  someone happened to check manually.
- The DAG only "works" when manually triggered by hand every time — not
  genuinely running unattended on its own schedule.
- An individual reflection that doesn't match the person's real git
  history at all.
