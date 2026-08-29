# Above & Beyond

Optional. Do these **after** MVP is genuinely solid — a shaky pipeline
with extra features isn't the goal. Pick 1-2, not all of them.

## A third real target, or a deeper rollup

Both required sources are the MVP bar now, not a stretch goal. Instead,
load one of your two sources into a **second** target table with a
different real grain (e.g. raw hourly Open-Meteo readings *and* a real
daily rollup, or raw NASA APOD rows *and* a real monthly summary). Show
it actually running, with real row counts for both grains.

## The ETL-vs-ELT tradeoff, written for your specific pipeline

Not the general definitions — this module's own `learning_objectives`
already have you evaluate that in the abstract. Write a short case
(half a page) for **your actual pipeline's real data volume and
latency profile**: given what you're really extracting and how often,
is your current ETL/ELT choice actually the right one? Would it still
be the right one at 100x the volume?

## What would this need at real production scale?

A short, written-only preview (half a page) of what this pipeline's
monitoring would genuinely need to look like if it ran in production —
not "add more monitoring," but specific: what real threshold would page
someone at 2am vs. what should just log and wait for morning, and why
that split makes sense for *your* pipeline's actual failure modes.

## MCP: what would it take for an agent to trigger this pipeline?

This module's own `ai_integration_notes` previews Model Context Protocol
(MCP) as an emerging way for an AI agent to call a pipeline's
tools/APIs directly, ahead of Module 13's fuller agentic-AI content.
Write a short case (half a page): if an agent could trigger your DAG on
demand instead of only on its schedule, what specific
monitoring-observability guardrail from *this* module would you need
before trusting it to do that unsupervised? Ground it in a real,
specific gap in your own pipeline's current logging/alerting — not a
generic "AI needs guardrails" claim.
