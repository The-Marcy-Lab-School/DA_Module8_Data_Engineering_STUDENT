# Team Charter & RACI

**Fill this in on Day 1-2, before any real DAG logic.** A charter
written after the build, to match who happened to touch what, doesn't
demonstrate real accountability — it's just a summary. This is graded
alongside the pipeline itself, and it's what your individual
accountability is checked against later.

## Team roster

| Name | Role |
|---|---|
| TODO | Project Manager |
| TODO | Technical Lead |
| TODO | Business Analyst |
| TODO | QA/Reliability Lead |

**At 3 people:** combine Project Manager and Business Analyst into one
role, and say so here explicitly — don't leave two names on one row and
call it done.

## RACI

For each real task, exactly one **R**esponsible-**A**ccountable owner
(they can be the same person, but there must be one clear **A** per
row) — the others are **C**onsulted or **I**nformed, or blank if truly
not involved. A row where every role is marked the same thing (all "R",
or all blank) isn't real accountability — it means no one actually owns
it.

| Task | Project Manager | Technical Lead | Business Analyst | QA/Reliability Lead |
|---|---|---|---|---|
| Open-Meteo extract → load path | | | | |
| NASA extract → load path | | | | |
| DAG orchestration (wiring both sources together) | | | | |
| ETL vs. ELT decision + justification | | | | |
| Retry/failure-handling design | | | | |
| Breaking the source on purpose (the real test) | | | | |
| Structured logging + alerting | | | | |
| CI gap: finding it | | | | |
| CI gap: fixing it + proving it | | | | |
| `backlog.md` | | | | |
| Branch protection setup | | | | |
| Final README (portfolio rewrite) | | | | |
| Group readout presentation | | | | |

## Why this split

**In your own words — why did you divide it this way?** Not "it seemed
fair" — a real reason tied to who's actually strongest where, or who
wanted to grow in which area.

TODO

## What happens if someone falls behind

**A real, specific plan** — not "we'll figure it out." Who notices
first (per the RACI above), what they do about it, and at what point it
becomes a milestone-check-in issue (see `backlog.md`).

TODO
