from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from medallion.bronze.projecttool import ingest


DAG_NAME = "bronze_projecttool_dag"


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
    schedule_interval=None,  # Only triggered by parent
    catchup=False
) as dag:
    import_tables_task = PythonOperator(
        task_id="import_tables",
        python_callable=ingest.import_tables,
        dag=dag,
    )

    import_tables_task
