from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from medallion.gold.gold_pr._gold_pr_dag import DAG_NAME as gold_pr_dag


DAG_NAME = "gold_dag"


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

    gold_pr = TriggerDagRunOperator(
        task_id=f"trigger_{gold_pr_dag}",
        trigger_dag_id=gold_pr_dag,
        wait_for_completion=True,
        poke_interval=5,
        conf={"message": "Start processing gold_pr"},
    )

    # ... other gold transformations

    gold_pr
