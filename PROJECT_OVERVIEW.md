# Project Overview: Data Engineering Pipelines & Delivery

**This is a team project.** 3-4 students, one shared repo, 4 named roles
with real, individually graded accountability.

## The objective

Build a real, scheduled, monitored, automated ETL/ELT pipeline in
**Apache Airflow** (via **Astro CLI**) that ingests from **both** of this
module's real external sources, transforms the data, and loads it into
your team's chosen **Module 3/7** data warehouse. Delivered with a
version-controlled, peer-reviewed GitHub repository (real feature-branch
+ pull-request workflow, enforced by real branch protection, reviewed by
real teammates) and a written project backlog/timeline and team charter
written *before* you start building, not after.

## Why it matters

This is the first project in the program that's genuinely operational,
not just analytical — a pipeline that has to keep running correctly
without you watching it, recover from real failures, and alert someone
when it can't. It's also the first **team** project in the program with
named roles and real, individually graded accountability — the same
shape a real data-platform team actually works in: a PM tracking scope
and timeline, a Technical Lead making architecture calls, a Business
Analyst translating the pipeline's purpose for a stakeholder, and a
QA/Reliability Lead making sure it doesn't silently break. **Module 9**
builds on this same orchestration instinct at cloud/distributed scale.

## Deliverables at a glance

- A real Airflow DAG, on a real schedule, running end-to-end with no
  manual intervention once triggered — extracting from **both** real
  external sources into two separate tables.
- Retries configured **and genuinely tested** against a real simulated
  failure — not just configured and assumed to work.
- Structured logging at every task; ≥1 real alert that fires on failure.
- A real GitHub Actions CI check, its one real gap identified and fixed.
- A real project backlog (`backlog.md`): ≥5 sequenced tasks with real
  estimates, written before the build, task order justified against the
  real deadline/dependency chain, each with a real owner from
  `team_charter.md`.
- A real, filled-in `team_charter.md` — a RACI table naming who's
  actually accountable for each real piece of this project.
- One shared git repo, built from scratch (no `.gitignore`/`LICENSE`
  given this time) — real feature-branch + pull-request workflow,
  enforced branch protection, real substantive review from teammates on
  every merge, a real proactive milestone check-in.
- Each member's own `individual_reflection.md` — real evidence of what
  they specifically owned and built.
- A group readout presentation, each role presenting their own piece.

## Skills you'll practice

- **ETL/ELT, Apache Airflow, Automation, Data Engineering** — a real,
  working, scheduled pipeline extracting from two real sources, not a
  diagram of one.
- **Monitoring & Observability** — real structured logs, a real alert.
- **CI/CD** — a real GitHub Actions workflow, a real gap found and
  closed.
- **Project Management, Prioritization** — a real backlog written first,
  task order justified against a real deadline, real ownership assigned
  per task.
- **Ownership & Accountability** — a real, proactive milestone check-in,
  and real individual evidence tied to your own RACI row.
- **Collaboration & Teamwork, Git Version Control** — a real
  feature-branch/PR workflow enforced by branch protection, real peer
  review from real teammates on every merge, not a single exchange.

## Timeline

9 days. See `CHECKLIST_TIMELINE.md` for the day-by-day sprint pace and
the full submission checklist.

## Where to start

Go to `README.md` to form your team and assign roles, then
`GETTING_STARTED.md` — Astro CLI setup (no sudo needed) and picking your
team's shared Module 3/7 warehouse. **Set up your team's git repo from
scratch this time** — `.gitignore`/`LICENSE` aren't given, a real second
rep of Module 0/4's own skill, done together this time.
