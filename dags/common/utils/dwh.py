import os


from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


conn_string = os.environ.get("AIRFLOW_CONN_POSTGRES_DWH")
engine: Engine = create_engine(conn_string)
