from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from medallion.silver.projecttool._silver_projecttool_dag import DAG_NAME as projecttool_dag


DAG_NAME = "silver_dag"


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(seconds=5),
}

with DAG(
    dag_id=DAG_NAME,
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval=None,  # Only triggered by parent
    catchup=False
) as dag:

    transform_projecttool = TriggerDagRunOperator(
        task_id=f"trigger_{projecttool_dag}",
        trigger_dag_id=projecttool_dag,
        wait_for_completion=True,
        poke_interval=5,
        conf={"message": "Start transform_projecttool"},
    )

    # ... other schemata systems

    transform_projecttool
