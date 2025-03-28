from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

from common.utils import reader


DAG_NAME = "silver_projecttool_dag"
POSTGRES_CONN_ID = "dwh_connection_postgres"
SQL_SCRIPT_PATH = "/opt/airflow/dags/medallion/silver/projecttool/setup.sql"


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
    setup_silver = SQLExecuteQueryOperator(
        task_id="setup_silver_projecttool",
        conn_id=POSTGRES_CONN_ID,
        sql=reader.readfile(SQL_SCRIPT_PATH),
        autocommit=True
    )

    stored_procedures = [
        "CALL public.prc_projecttool_silver_users()",
        "CALL public.prc_projecttool_silver_projects()",
        "CALL public.prc_projecttool_silver_businesspartners()",
        "CALL public.prc_projecttool_silver_projecttimes()"
    ]

    stored_procedure_tasks = []
    for i, sp in enumerate(stored_procedures):
        task = SQLExecuteQueryOperator(
            task_id=f"execute_stored_procedure_{i}",
            conn_id=POSTGRES_CONN_ID,
            sql=sp,
            autocommit=True
        )
        stored_procedure_tasks.append(task)

    setup_silver >> stored_procedure_tasks
