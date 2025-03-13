from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.utils.dates import days_ago
from medallion.bronze._bronze_dag import DAG_NAME as bronze_dag_name
from medallion.silver._silver_dag import DAG_NAME as silver_dag_name
from medallion.gold._gold_dag import DAG_NAME as gold_dag_name


with DAG(
    dag_id="master_dag",
    start_date=days_ago(1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    trigger_bronze = TriggerDagRunOperator(
        task_id=f"trigger_{bronze_dag_name}",
        trigger_dag_id=bronze_dag_name,
        wait_for_completion=True,
        poke_interval=10,
        conf={"message": "Start Bronze Processing"},
    )

    trigger_silver = TriggerDagRunOperator(
        task_id=f"trigger_{silver_dag_name}",
        trigger_dag_id=silver_dag_name,
        wait_for_completion=True,
        poke_interval=10,
        conf={"message": "Start Silver Processing"},
    )

    trigger_gold = TriggerDagRunOperator(
        task_id=f"trigger_{gold_dag_name}",
        trigger_dag_id=gold_dag_name,
        wait_for_completion=True,
        poke_interval=10,
        conf={"message": "Start Gold Processing"},
    )

    trigger_bronze >> trigger_silver >> trigger_gold
