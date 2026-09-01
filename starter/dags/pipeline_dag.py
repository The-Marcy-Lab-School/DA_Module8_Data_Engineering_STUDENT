"""
GIVEN TEMPLATE -- the real structure a working Airflow DAG needs
(decorators, task wiring, retry/logging config points), with the actual
extract/transform/load logic left as TODOs, for ONE source. This mirrors
objective 1's own "following a provided DAG template" guided rep -- your
team's real independent work is to fill this in for your first source
AND build a real, parallel extract/transform/load path for your second
required source (see SCENARIOS.md -- both Open-Meteo and NASA are
required), wired into this same DAG. Don't just fill in these TODOs and
call the project done; this file is your mechanical starting point for
one path, not your whole graded deliverable.

Real, verified pattern (this exact structure, for both sources, was
built and run for real before this template was written -- see
../../../instructor/solution/ if you're the instructor reading this).
"""
from __future__ import annotations

import logging

import pendulum
from airflow.sdk import dag, task

log = logging.getLogger(__name__)


@dag(
    dag_id="pipeline_dag",
    # TODO: pick a real schedule for your real source's real update
    # cadence -- "@daily" is a placeholder, not necessarily correct for
    # your source.
    schedule="@daily",
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    catchup=False,
    default_args={
        # TODO: these are placeholder retry values. A real retry
        # strategy needs a real reason behind the numbers -- and per
        # required_components.md, you need to ACTUALLY test that a
        # retry fires and recovers, not just set these and move on.
        "retries": 2,
        "retry_delay": pendulum.duration(minutes=2),
    },
)
def pipeline_dag():

    @task
    def extract():
        """TODO: call your real external source's real API.
        Raise a real exception (don't silently swallow errors) if the
        request fails -- that's what makes retries meaningful."""
        raise NotImplementedError("TODO: implement extract()")

    @task
    def transform(raw):
        """TODO: shape the raw response into the real rows your load
        step needs. Log a real row count here (log.info(...)) -- this
        is part of the structured-logging requirement, not optional."""
        raise NotImplementedError("TODO: implement transform()")

    @task
    def load(rows):
        """TODO: load into your own Module 3/8 warehouse -- reuse the
        same connection approach from Module 4/8 (read credentials from
        the environment, never hardcode them). Return a real row count
        so it shows up in the task's XCom / logs."""
        raise NotImplementedError("TODO: implement load()")

    load(transform(extract()))


pipeline_dag()
