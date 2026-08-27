# Required Components

Every one of these must be real and demonstrated — not asserted. Fill in
what you actually built/found for each section; this is graded alongside
the pipeline itself.

## 1. The pipeline (extract → transform → load)

**Your real external source, and why you picked it:** TODO

**Which approach your pipeline uses — ETL or ELT — and why** (tie it to
your real source/target and actual data volume/latency, not a generic
answer): TODO

**Your target table, in your own Module 3/7 warehouse:** TODO

**Real row count from an actual triggered run** (query your target table
directly, paste the real result): TODO

## 2. Failure handling — a real test, not a configured-and-assumed one

The single most common failure on this section: retries configured but
never actually tested. Don't let that be you.

**How you broke the source on purpose** (a real, specific action — rename
a column, kill the connection mid-run, point at a bad URL): TODO

**What actually happened** — paste the real task log/error, and confirm
whether the retry actually fired and whether it recovered or correctly
failed after exhausting retries: TODO

## 3. Monitoring & alerting

**Where structured logs are emitted, and what they actually say** (paste
a real log line per task, not a description of what you'd expect to
see): TODO

**Your real alert, and how you confirmed it actually fires on failure**
(not just configured): TODO

## 4. The CI gap

**What was actually missing from the given `.github/workflows/ci.yml`,**
and why it matters (what could pass the old CI and still be broken)?
TODO

**Your fix, and proof it works**: trigger a PR with a deliberately broken
DAG, paste the real CI failure output, then fix it and paste the real
CI success output. Two real runs, not one assumed.

## 5. Project management

**Link to `backlog.md`** — this file should already exist and be filled
in from before you started building, not backfilled now.

## 6. Git collaboration (a real partner exercise)

**Your partner:** TODO

**The real feature branch + PR you built together:** TODO — link it.

**The substantive review comment you gave them** (paste it — "LGTM"
doesn't count): TODO

**The real peer comment you received and incorporated** (paste it, and
what you changed in response): TODO

**Your milestone check-in** — see `backlog.md`'s own section for this;
confirm here that it was reported proactively, not after being asked.
