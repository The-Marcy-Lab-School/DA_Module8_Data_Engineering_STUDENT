"""GIVEN, real, working test -- confirms every DAG in dags/ actually
parses/imports without error. This is the real check that's currently
MISSING from .github/workflows/ci.yml -- see required_components.md's
CI-gap exercise. A DAG can pass a linter (syntactically valid, styled
correctly) while still being structurally broken in a way only Airflow
itself would catch (a bad schedule value, a missing required argument,
a real import error) -- lint passing is not the same as "this DAG would
actually load."
"""
from airflow.models import DagBag


def test_no_import_errors():
    dagbag = DagBag(dag_folder="dags/", include_examples=False)
    assert dagbag.import_errors == {}, (
        f"DAG import errors found: {dagbag.import_errors}"
    )


def test_at_least_one_dag_loaded():
    dagbag = DagBag(dag_folder="dags/", include_examples=False)
    assert len(dagbag.dags) >= 1, "No DAGs were found in dags/"
