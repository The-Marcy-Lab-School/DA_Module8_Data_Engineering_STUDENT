# Getting Started

## "Use this template" vs. Fork vs. Clone

Same rule as every project: **"Use this template"** on this repo's GitHub
page (not Fork) creates your own independent copy. Clone *that* copy, not
this template directly.

## Prerequisite: Docker

Astro CLI runs Airflow locally via Docker containers. If you don't
already have Docker Desktop, install it first — everything below assumes
`docker` works from your terminal.

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

## Reconnect to your Module 3/7 warehouse

**Same real database from Module 3, the same one your Module 7 dbt
project ran against — not a new one.** Your DAG's `load` task needs to
connect to it directly (via `psycopg2`, the same library from Module 4)
— read the connection details from environment variables, never
hardcode them (this module's own `common_project_mistakes`-adjacent
habit, carried from every prior module).

1. Confirm it's still reachable: `psql <your connection string>`.
2. Set the connection details as environment variables your DAG code can
   read — **do not put real credentials in a file this repo tracks.**
   Astro CLI supports a local `.env` file for exactly this (already
   listed in what your own `.gitignore` should exclude — see
   `README.md` Step 3).

## Your real external source

See `SCENARIOS.md` for the two real, verified options (Open-Meteo — no
API key needed, recommended default; NASA — free key required). Pick
one before you start building the real DAG logic.

## What's next

Once `astro dev start` shows a real Airflow UI and your database is
reachable, go back to `README.md`'s "What to do" section and start with
`backlog.md`.
