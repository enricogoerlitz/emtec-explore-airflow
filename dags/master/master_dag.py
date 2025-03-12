from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.utils.dates import days_ago

with DAG(
    dag_id="master_dag",
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False
) as dag:

    trigger_bronze = TriggerDagRunOperator(
        task_id="trigger_bronze_dag",
        trigger_dag_id="bronze_dag",
        wait_for_completion=True,
        conf={"message": "Start Bronze Processing"},
    )

    trigger_silver = TriggerDagRunOperator(
        task_id="trigger_silver_dag",
        trigger_dag_id="silver_dag",
        wait_for_completion=True
    )

    trigger_gold = TriggerDagRunOperator(
        task_id="trigger_gold_dag",
        trigger_dag_id="gold_dag",
        wait_for_completion=True
    )

    trigger_bronze >> trigger_silver >> trigger_gold
