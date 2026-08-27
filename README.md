# Data Engineering Pipelines & Delivery Project

Start with `PROJECT_OVERVIEW.md` for what you're building and why. This
file (`README.md`) is where the step-by-step setup lives.

**Due:** 8 days, run as a sprint. See `CHECKLIST_TIMELINE.md` for the
day-by-day pace and the full submission checklist.

This repo is a **GitHub template** — a starting point, not something you
edit directly on Marcy's copy of it.

## Getting started

### Step 1: Get your own copy

On this repo's GitHub page, click **"Use this template" → "Create a new
repository"** (not Fork). Name it something like `data-engineering-pipeline`,
keep it **public**, and create it.

### Step 2: Clone your new repo locally

```bash
git clone <the URL of your own new repo>
cd <your-repo-name>
```

### Step 3: Set up git yourself — this module tests it again

Unlike Module 3/5/6/7, this repo does **not** come with `.gitignore` or
`LICENSE` already made — `git-version-control` is being tested again,
this time expecting real independence (a third rep, after Module 0's
first-ever pass and Module 4's second one).

- **Create a `.gitignore`.** Think about what this specific project
  shouldn't track — `.env` (real credentials), `.astro/`, `logs/`,
  `__pycache__/`, OS files. Write it yourself.
- **Choose a `LICENSE`.** Same call as every prior project.
- **`git init`, commit both, then keep committing atomically as you go.**

#### What your repo should look like once this step is done

```
your-repo-name/
├── .gitignore              ← you create this
├── LICENSE                 ← you create this
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
    ├── required_components.md     ← already here
    ├── .github/workflows/ci.yml   ← already here
    └── tests/dags/test_dag_integrity.py ← already here
```

### Step 4: Set up Astro CLI

See `GETTING_STARTED.md` — Astro CLI (Airflow) is new this module and
gets its own dedicated setup walkthrough (real, confirmed: no `sudo`
needed).

### Step 5: Reconnect to your Module 3/7 warehouse

Also in `GETTING_STARTED.md` — the same database you built in Module 3
and built a real dbt project against in Module 7.

## Find a real partner — this module needs one

This module's real partner-collaboration requirement (and the
`collaboration-teamwork`/`git-version-control` grading) needs a **real
second person**: someone gives you a real, substantive pull-request
review comment, and you give one back. Pick a partner before Day 6 (see
`CHECKLIST_TIMELINE.md`) — this isn't something you can simulate solo.
The mechanic: pick one of your two repos, add each other as a
collaborator, and each of you opens one real feature-branch PR with a
small, real, useful addition to that pipeline (an extra data-quality
check, a second alert, anything real) — review each other's PR for
real, incorporate the feedback, merge.

## What to do

- `starter/dags/pipeline_dag.py` is a **given template** — real
  structure (decorators, retry config points, task wiring), the actual
  extract/transform/load logic left as `TODO`/`NotImplementedError`.
  Following it is the guided rep; your real, independent project needs
  more than filling in these three TODOs — your instructor's shared
  checklist has the full required scope.
- Write `backlog.md` **before** you write real DAG logic — a strong
  submission can point to a specific backlog task for every hour spent.
- Build the real pipeline: extract from a real external source (see
  `SCENARIOS.md` for the two verified options), transform, load into
  your own warehouse.
- Configure retries, structured logging, and ≥1 real alert — then
  **actually break your source on purpose** and confirm the failure
  handling does what you designed (`required_components.md` Section 2).
- `starter/.github/workflows/ci.yml` is **given, real, and running** —
  but has one real gap (see `required_components.md` Section 4). Find
  it, name it, fix it, prove the fix with two real CI runs.
- Do the real partner PR exchange (above).
- Fill in `required_components.md` as you go, not from memory at the
  end.

`CHECKLIST_TIMELINE.md` has the suggested day-by-day pace and the full
sequenced checklist.

**Where's the exact bar for "done," and what are the optional stretch
goals?** This repo (your own copy) doesn't include `MVP.md` (your **M**inimum **V**iable **P**roduct —
the required baseline) or `ABOVE_AND_BEYOND.md` on purpose — they're not something to keep sitting
in your portfolio repo. Ask your instructor for the link to this
template's `project-scope` branch to read them, or check the checklist
your instructor shares through the classroom, which covers the same
ground.
