# MVP — the real bar for "done"

This is what actually gets graded as Meets/Approaching/Below per skill.
See instructor `rubric.md` for the full rubric if your instructor has
shared it — this is the same bar in checklist form.

## The pipeline

- [ ] A real Airflow DAG, on a real schedule (`@daily`/`@hourly`), that
      runs end-to-end with **no manual intervention** once triggered.
- [ ] Extract from your real chosen external source (`SCENARIOS.md`);
      transform in a real Python task; load into a **new table** in your
      own Module 3/7 warehouse — real row counts land, confirmed with a
      direct `SELECT`, not just "the task turned green."
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

## Project management

- [ ] `backlog.md` written **before** any real DAG logic (per this
      module's own `exemplar_guidance`) — ≥5 discrete, sequenced tasks
      with real estimated durations.
- [ ] Task order in the backlog is **justified against the real
      deadline and dependency chain** — not just listed arbitrarily
      (e.g., "build extract task" genuinely precedes "write monitoring
      alerts" because monitoring needs something to monitor).
- [ ] A real, proactive milestone check-in (on track / at risk, with a
      specific reason if at risk) — reported before being asked, not
      backfilled at the end.

## Git & collaboration

- [ ] Your own `.gitignore`/`LICENSE`, written from scratch — real work
      always happens on a feature branch, never directly on `main`.
- [ ] A real partner PR exchange (see `README.md`): one real,
      substantive review comment given, one real peer comment received
      and visibly incorporated into the merged code. Pull requests are
      merged only after real review — not a single self-approved commit
      with no peer comment.

## Written work

- [ ] `starter/required_components.md` — all 6 sections filled in for
      real, as you go (not from memory at the end): the real pipeline
      and its real row count, the real break-it-on-purpose test and what
      actually happened, the real monitoring/alert evidence, the real CI
      gap and its fix, the backlog link, and the real partner-PR record.

## What "Below" looks like, concretely

- Retries configured but never actually tested against a real failure.
- The backlog written retroactively, after the pipeline already works,
  instead of before starting the build.
- A pull request that's a single self-approved commit with no real peer
  review.
- No alerting configured, so a failed run would go unnoticed until
  someone happened to check manually.
- The DAG only "works" when manually triggered by hand every time — not
  genuinely running unattended on its own schedule.
