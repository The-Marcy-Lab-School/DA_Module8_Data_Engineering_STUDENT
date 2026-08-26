# Checklist & Timeline

**8 days, run as a sprint.** This is the most operationally complex
project in the program so far (11 real skills tested) — real setup cost
on Days 1-2 is expected, not falling behind.

## Day 1 — Git setup, Astro, reconnect, backlog

- [ ] Real `.gitignore`/`LICENSE` created yourself, first commits made.
- [ ] `astro dev start` shows a real Airflow UI.
- [ ] Confirmed your Module 3/7 database is reachable.
- [ ] Picked your real external source (`SCENARIOS.md`).
- [ ] **`backlog.md` written** — before any real DAG logic.
- [ ] **Find your partner** — don't wait until Day 6 for this.

## Day 2-3 — The real pipeline

- [ ] `extract`/`transform`/`load` implemented for real (replacing the
      given template's TODOs) — a real, triggered run lands real rows in
      your warehouse.
- [ ] DAG runs on a real schedule, no manual triggering needed after the
      first confirm.

## Day 4 — Failure handling, for real

- [ ] Retries configured with a real, reasoned strategy (not placeholder
      defaults left as-is).
- [ ] **Actually break your source on purpose** — rename a column, kill
      the connection, point at a bad URL. Confirm what actually happens
      (`required_components.md` Section 2).

## Day 5 — Monitoring, CI gap

- [ ] Structured logs at every task.
- [ ] ≥1 real alert, confirmed to actually fire on a real failure.
- [ ] Found and named the real gap in `.github/workflows/ci.yml`.
- [ ] Fixed it — two real CI runs (broken, then fixed) as proof.

## Day 6-7 — Partner PR exchange

- [ ] Real feature branch, real PR, on one of your two repos.
- [ ] A real, substantive review comment given.
- [ ] A real peer comment received and incorporated.
- [ ] Merged.

## Day 8 — Finish, milestone check-in, submit

- [ ] Milestone check-in reported proactively in `backlog.md` (not
      backfilled).
- [ ] `required_components.md` fully filled in with real evidence.
- [ ] Commit and push.

## Submission checklist

- [ ] A real, scheduled DAG, running end-to-end with no manual
      intervention.
- [ ] Retries genuinely tested against a real simulated failure.
- [ ] Structured logging + ≥1 real, confirmed-firing alert.
- [ ] The real CI gap found and fixed, proven with two real runs.
- [ ] `backlog.md` — ≥5 real, sequenced, estimated tasks, written first.
- [ ] Real git history: your own `.gitignore`/`LICENSE`, feature-branch +
      PR workflow, never directly on `main`.
- [ ] A real partner PR exchange — given and received.
- [ ] **Delete `PROJECT_OVERVIEW.md` and `SCENARIOS.md`** — they explain
      the assignment, not your project; a real portfolio repo shouldn't
      have "here's what you were asked to build" sitting in it.
- [ ] **Replace `README.md`'s content with your own real project README**
      — write it for someone who's never seen this assignment:
  - **Pipeline Purpose** — what real data it moves, and why.
  - **Architecture Overview** — the DAG's real tasks and dependencies.
  - **Design Decisions** — your retry/failure-handling approach and why.
  - **Monitoring & Reliability Approach** — your real alert, what it
    catches.
- [ ] A real, proactive milestone check-in.
