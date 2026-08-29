# Checklist & Timeline

**9 days, run as a sprint, as a team of 3-4.** This is the most
operationally complex project in the program so far (11 real skills
tested) — real setup cost on Days 1-2 is expected, not falling behind.
Every day below names which role typically drives it, but the whole
team should understand the whole pipeline by the end.

## Day 1 — Form the team, roles, repo setup

- [ ] Team formed (3-4), roles assigned — PM, Technical Lead, Business
      Analyst, QA/Reliability Lead (3-person teams: PM+BA combined).
- [ ] **One shared repo** created (PM), collaborators added, **branch
      protection on `main`** turned on (require 1 approving review).
- [ ] Real `.gitignore`/`LICENSE` created together, first commits made,
      every member's name on the `LICENSE` copyright line.
- [ ] Team picked **one** member's Module 3/7 warehouse; access shared
      securely (not committed, not in a public channel).
- [ ] **`team_charter.md` written** — the real RACI, before any DAG code.
- [ ] **`backlog.md` written** — before any real DAG logic, tasks tied to
      real owners from the charter.

## Day 2-3 — Astro setup + both real pipelines

- [ ] `astro dev start` shows a real Airflow UI (everyone, locally).
- [ ] Confirmed the team's chosen warehouse is reachable from everyone's
      own machine.
- [ ] **Both** real external sources' `extract`/`transform`/`load` paths
      implemented for real (Open-Meteo and NASA, per `SCENARIOS.md`) —
      each owned by a different team member, a real triggered run lands
      real rows in two separate tables.
- [ ] DAG runs on a real schedule, no manual triggering needed after the
      first confirm — Technical Lead owns wiring both paths into one DAG.
- [ ] **Stated and justified which approach — ETL or ELT — your pipeline
      actually uses**, tied to your real source/target and data
      volume/latency, not a default guess (`required_components.md`
      Section 1). This is a required part of passing, not a bonus.

## Day 4 — Failure handling, for real

- [ ] Retries configured with a real, reasoned strategy (not placeholder
      defaults left as-is).
- [ ] **Actually break a source on purpose** — rename a column, kill the
      connection, point at a bad URL. Confirm what actually happens
      (`required_components.md` Section 2). QA/Reliability Lead drives
      this.

## Day 5 — Monitoring, CI gap

- [ ] Structured logs at every task.
- [ ] ≥1 real alert, confirmed to actually fire on a real failure.
- [ ] Found and named the real gap in `.github/workflows/ci.yml`.
- [ ] Fixed it — two real CI runs (broken, then fixed) as proof.

## Day 6-7 — Real PR review, every merge

- [ ] Every feature branch merged only after a real, substantive review
      from a teammate — branch protection enforces this, but check it's
      actually happening, not rubber-stamped.
- [ ] ≥2 real, substantive review comments given (not "LGTM"), by ≥2
      different team members.
- [ ] ≥2 real peer comments received and incorporated.

## Day 8 — Finish, milestone check-in

- [ ] Milestone check-in reported proactively in `backlog.md` (not
      backfilled) — PM posts it, reflecting the whole team's real status.
- [ ] `required_components.md` fully filled in with real evidence.
- [ ] Each member's own `individual_reflection_<name>.md` filled in.
- [ ] Commit and push.

## Day 9 — Group readout, submit

- [ ] **Group readout presentation**: PM opens with scope/timeline, Tech
      Lead covers architecture, Business Analyst covers what the pipeline
      serves and why, QA/Reliability Lead covers failure-handling and
      monitoring. Each person fields Q&A on their own piece.

## Submission checklist

- [ ] A real, scheduled DAG, running end-to-end with no manual
      intervention, extracting from **both** real sources.
- [ ] Your ETL vs. ELT choice, stated and justified against your real
      source/target and volume/latency (`required_components.md`
      Section 1).
- [ ] Retries genuinely tested against a real simulated failure.
- [ ] Structured logging + ≥1 real, confirmed-firing alert.
- [ ] The real CI gap found and fixed, proven with two real runs.
- [ ] `backlog.md` — ≥5 real, sequenced, estimated, owned tasks, written
      first.
- [ ] `team_charter.md` — a real RACI, one clear accountable owner per
      row, not everyone marked the same on every task.
- [ ] Real git history: shared `.gitignore`/`LICENSE`, feature-branch +
      PR workflow enforced by branch protection, never directly on
      `main`.
- [ ] ≥2 real PR reviews given, ≥2 received and incorporated, by
      different team members.
- [ ] Every member's own `individual_reflection_<name>.md` present and
      specific, not copy-pasted between teammates.
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
  - **Team & Roles** — who owned what, linking back to your real RACI.
- [ ] A real, proactive milestone check-in.
- [ ] **Non-PM members**: fork the finished repo to your own GitHub
      before the deadline, so it's part of your own portfolio too.
