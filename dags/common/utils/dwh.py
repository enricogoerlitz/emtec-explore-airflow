import os


from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine


base_conn_string = os.environ.get("AIRFLOW_CONN_POSTGRES_DWH")

BASE_DATABASE = "datawarehouse"
BRONZE_DATABASE = "bronze"
SILVER_DATABASE = "silver"
GOLD_DATABASE = "gold"


def engine(database: str) -> Engine:
    conn_string = base_conn_string.replace(BASE_DATABASE, database)

    return create_engine(conn_string)


class DataWarehouseConnector:
    _dwh: Engine = None
    _bronze_engine: Engine = None
    _silver_engine: Engine = None
    _gold_engine: Engine = None

    @property
    def dwh_engine(self) -> Engine:
        if not self._dwh:
            self._dwh = engine(BASE_DATABASE)

        return self._dwh

    @property
    def bronze_engine(self) -> Engine:
        if not self._bronze_engine:
            self._bronze_engine = engine(BRONZE_DATABASE)

        return self._bronze_engine

    @property
    def silver_engine(self) -> Engine:
        if not self._silver_engine:
            self._silver_engine = engine(SILVER_DATABASE)

        return self._bronze_engine

    @property
    def gold_engine(self) -> Engine:
        if not self._gold_engine:
            self._gold_engine = engine(GOLD_DATABASE)

        return self._bronze_engine

    def create_schema_if_not_exists(self, engine: Engine, schema: str):
        with engine.begin() as conn:
            conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema}"))


dwh = DataWarehouseConnector()
