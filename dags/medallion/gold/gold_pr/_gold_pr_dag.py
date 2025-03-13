from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


DAG_NAME = "gold_pr_dag"
POSTGRES_CONN_ID = "dwh_connection_postgres"


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(seconds=5),
}

with DAG(
    dag_id=DAG_NAME,
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval=None,  # Only triggered manually or by a parent DAG
    catchup=False,
) as dag:
    refresh_materialized_views = [
        "REFRESH MATERIALIZED VIEW gold_pr.DimProjects",
        "REFRESH MATERIALIZED VIEW gold_pr.DimUsers",
        "REFRESH MATERIALIZED VIEW gold_pr.FactProjecttimes",
    ]

    stored_procedure_tasks = []
    for i, sql in enumerate(refresh_materialized_views):
        task = SQLExecuteQueryOperator(
            task_id=f"refresh_materialized_view_{i}",
            conn_id=POSTGRES_CONN_ID,
            sql=sql,
            autocommit=True
        )
        stored_procedure_tasks.append(task)

    stored_procedure_tasks
