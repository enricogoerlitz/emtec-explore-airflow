import os


from sqlalchemy import create_engine
from sqlalchemy.engine import Engine, text


conn_string = os.environ.get("AIRFLOW_CONN_POSTGRES_DWH")
engine: Engine = create_engine(conn_string)


def ensure_schema_exists(schema: str):
    with engine.begin() as conn:  # ✅ Correct: Automatically commits
        conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema}"))
