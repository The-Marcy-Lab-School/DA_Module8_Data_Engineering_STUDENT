# Getting Started

## "Use this template" vs. Fork vs. Clone

Same rule as every project, with one team-project difference: the
**Project Manager** clicks **"Use this template"** (not Fork) on this
repo's GitHub page, creating **one** repo for the whole team. The PM adds
the rest of the team as collaborators; everyone clones that **same**
repo, not their own separate copy.

## Prerequisite: Docker

Astro CLI runs Airflow locally via Docker containers. If you don't
already have Docker Desktop, install it first — everything below assumes
`docker` works from your terminal.

**Real memory requirement, confirmed by actually measuring it:** a
running local Airflow stack (scheduler, triggerer, dag-processor,
API server, its own Postgres) uses about **2GB of RAM on its own** --
before your own DAG does anything. This is fixed orchestrator overhead,
not something that scales with how much data your pipeline moves.
Before `astro dev start`, open Docker Desktop's Settings → Resources and
confirm it's allotted **at least 4GB** (8GB+ total system RAM
recommended) -- if it's set lower (a common fresh-install default),
raise it there, not by changing anything in this project. If containers
keep getting killed or `astro dev start` hangs, this is almost always
why -- check Docker Desktop's resource allocation and how much else you
have open (extra browser windows, other VMs, etc.) before assuming your
DAG code is the problem.

## Set up Astro CLI

**Confirmed working without `sudo`** (the official one-line installer
asks for root, but you don't need it):

```bash
curl -sL -o- https://raw.githubusercontent.com/astronomer/astro-cli/main/godownloader.sh | bash -s -- -b ~/.local/bin
# make sure ~/.local/bin is on your PATH -- add this to your shell profile if it isn't:
export PATH="$HOME/.local/bin:$PATH"
astro version
```

From this repo's root:

```bash
astro dev start
```

**First run genuinely takes a few minutes** — it's pulling a real
container image and starting a full local Airflow stack (scheduler,
triggerer, a UI, its own metadata database). Once it's done, the command
prints a real URL (`http://localhost:8080` by default) — open it, you
should see a real Airflow UI with `pipeline_dag` listed (paused, since
you haven't finished it yet).

`astro dev stop` shuts everything down when you're done for the day —
run it, don't just close your terminal, or the containers keep running.

## Whose warehouse? Pick one, share access to it securely

Each of you has your **own** Module 3/7 warehouse from earlier in the
program — four separate databases. This pipeline loads into **one**
team warehouse, not four. Pick one member's (doesn't have to be the
Technical Lead's, but that's the natural default) and use it for the
whole project.

**Real reason this matters, and a real skill in its own right**: sharing
database access securely across a team — without anyone hardcoding
someone else's password into a file that gets committed — is exactly
what real data teams do constantly. The mechanic:

1. The warehouse owner confirms it's still reachable:
   `psql <their connection string>`.
2. The warehouse owner shares the connection details (host, port, db
   name, user, password) with the rest of the team through a real
   secure channel — a password manager's shared vault, or a DM, not a
   Slack channel everyone can see, and **never a commit**.
3. Each teammate sets those same connection details as environment
   variables their own local Astro CLI run can read — **do not put real
   credentials in a file this repo tracks.** Astro CLI supports a local
   `.env` file for exactly this (already listed in what your own
   `.gitignore` should exclude — see `README.md` Step 4). Since `.env`
   is gitignored, each teammate creates their own local copy from the
   same shared values — it never gets committed or merged by anyone.

## Your real external sources — both, this time

See `SCENARIOS.md` for the two real, verified options (Open-Meteo — no
API key needed; NASA — free personal key required, get one at
`api.nasa.gov`, costs nothing). **Both are required** — this pipeline
extracts from both sources into two separate tables in the team
warehouse, not just one. Divide the two extract→load paths between two
team members before you start building the real DAG logic; the
Technical Lead owns wiring both into one working DAG.

## What's next

Once `astro dev start` shows a real Airflow UI and your database is
reachable, go back to `README.md`'s "What to do" section and start with
`backlog.md`.
