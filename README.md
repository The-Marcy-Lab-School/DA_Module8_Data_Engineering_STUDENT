# Data Engineering Pipelines & Delivery Project

**This is a team project — 3-4 students, one shared repo.** Start with
`PROJECT_OVERVIEW.md` for what you're building and why, and
`starter/team_charter.md` for how the 4 roles (Project Manager,
Technical Lead, Business Analyst, QA/Reliability Lead) split
accountability. This file (`README.md`) is where the step-by-step setup
lives.

**Due:** 9 days, run as a sprint. See `CHECKLIST_TIMELINE.md` for the
day-by-day pace and the full submission checklist.

This repo is a **GitHub template** — a starting point, not something you
edit directly on Marcy's copy of it.

## Getting started

### Step 1: Form your team and assign roles

3-4 students. One person per role — **Project Manager**, **Technical
Lead**, **Business Analyst**, **QA/Reliability Lead**. At 3 people, PM
and Business Analyst combine into one role (the lightest individual
technical load of the four) — say so explicitly in `team_charter.md`,
don't leave it implicit.

### Step 2: Get your team's copy

**One repo for the whole team, not one each.** The Project Manager
clicks **"Use this template" → "Create a new repository"** (not Fork)
on this repo's GitHub page. Name it something like
`data-engineering-pipeline-team`, keep it **public**, and create it.

Then, on the new repo's **Settings → Collaborators**, the PM adds the
other 2-3 team members with write access. Everyone clones the **same**
repo:

```bash
git clone <the URL of your team's new repo>
cd <your-repo-name>
```

### Step 3: Turn on branch protection — real enforcement, not an honor system

PM does this once, in the team repo's **Settings → Branches**: add a
protection rule on `main` requiring **at least 1 approving review**
before merge, and disable direct pushes to `main`. This is what makes
the PR-review requirement below actually enforced by GitHub, not just a
rule everyone's supposed to remember.

### Step 4: Set up git — this module tests it again

Unlike Module 3/5/6/7, this repo does **not** come with `.gitignore` or
`LICENSE` already made — `git-version-control` is being tested again,
this time expecting real independence (a third rep, after Module 0's
first-ever pass and Module 4's second one). **One person does this
first** (whoever's fastest to clone), commits it, everyone else pulls.

- **Create a `.gitignore`.** Think about what this specific project
  shouldn't track — `.env` (real credentials), `.astro/`, `logs/`,
  `__pycache__/`, OS files. Write it yourselves.
- **Choose a `LICENSE`.** Same call as every prior project — but this
  time list every team member's name on the copyright line, not just
  one.
- **`git init`, commit both, then keep committing atomically as you go**
  — on feature branches, never directly on `main` (branch protection
  now enforces this for real).

#### What your repo should look like once this step is done

```
your-repo-name/
├── .gitignore              ← you create this
├── LICENSE                 ← you create this, every member's name on it
├── README.md               ← already here
├── PROJECT_OVERVIEW.md     ← already here
├── GETTING_STARTED.md      ← already here
├── CHECKLIST_TIMELINE.md   ← already here
├── SCENARIOS.md            ← already here (real external source options)
└── starter/
    ├── dags/pipeline_dag.py       ← already here (fill in)
    ├── requirements.txt           ← already here
    ├── Dockerfile                 ← already here
    ├── backlog.md                 ← already here (fill in)
    ├── team_charter.md            ← already here (fill in — your RACI)
    ├── individual_reflection.md   ← already here (each member fills their own copy)
    ├── required_components.md     ← already here
    ├── .github/workflows/ci.yml   ← already here
    └── tests/dags/test_dag_integrity.py ← already here
```

### Step 5: Set up Astro CLI

See `GETTING_STARTED.md` — Astro CLI (Airflow) is new this module and
gets its own dedicated setup walkthrough (real, confirmed: no `sudo`
needed). Everyone installs it locally — the shared repo is one codebase,
but each of you runs it on your own machine.

### Step 6: Pick and connect to the team's warehouse

Also in `GETTING_STARTED.md` — your team picks **one member's** existing
Module 3/7 warehouse to use for this project (not four separate
databases), and shares access to it securely. Read that section before
anyone starts writing DAG code.

## Roles and accountability — `team_charter.md`

Fill in `starter/team_charter.md` — a real RACI table — on Day 1-2,
**before** any real DAG logic. It names who's actually accountable for
each real task (both sources' extract/load, orchestration, failure
handling, CI, monitoring, the final docs, the group readout). This isn't
paperwork: it's what "individual accountability" is graded against later
(see `instructor`'s shared rubric) — a charter where everyone's listed as
accountable for everything fails that check.

## What to do

- `starter/dags/pipeline_dag.py` is a **given template** — real
  structure (decorators, retry config points, task wiring), the actual
  extract/transform/load logic left as `TODO`/`NotImplementedError`.
  Following it is the guided rep; your real, independent team project
  needs more than filling in these three TODOs — your instructor's
  shared checklist has the full required scope.
- Write `backlog.md` **before** you write real DAG logic — a strong
  submission can point to a specific backlog task, and a specific owner
  from `team_charter.md`, for every hour spent.
- Build the real pipeline: extract from **both** real external sources
  (see `SCENARIOS.md`) — Open-Meteo and NASA — each with its own
  extract→load path into a new table, transform, load into your team's
  chosen warehouse. One team member owns each source's path; the
  Technical Lead owns wiring both into one DAG.
- Configure retries, structured logging, and ≥1 real alert — then
  **actually break your source on purpose** and confirm the failure
  handling does what you designed (`required_components.md` Section 2).
- `starter/.github/workflows/ci.yml` is **given, real, and running** —
  but has one real gap (see `required_components.md` Section 4). Find
  it, name it, fix it, prove the fix with two real CI runs.
- **Real PR review on every merge** — every feature branch gets a real,
  substantive review from a teammate before merging (branch protection
  enforces this). Not one exchange with one partner — this is how the
  whole team's work gets merged, the entire sprint.
- Fill in `required_components.md` and `individual_reflection.md` (your
  own copy) as you go, not from memory at the end.

`CHECKLIST_TIMELINE.md` has the suggested day-by-day pace and the full
sequenced checklist.

**Where's the exact bar for "done," and what are the optional stretch
goals?** This repo (your own copy) doesn't include `MVP.md` (your
**M**inimum **V**iable **P**roduct — the required baseline) or
`ABOVE_AND_BEYOND.md` on purpose — they're not something to keep sitting
in your portfolio repo. Ask your instructor for the link to this
template's `project-scope` branch to read them, or check the checklist
your instructor shares through the classroom, which covers the same
ground.

**A note for non-PM team members**: since this is one shared repo, only
the PM's GitHub account shows it natively. Before the final submission
deadline, fork the finished repo to your own GitHub so it's part of
your own portfolio too — your real commit history inside it is what
proves your own contribution either way.
