import pandas as pd

from common.daglogging import logger
from common.utils import dwh


SCHEMA_NAME = "projecttool"
SOURCE_FILEPATH = "/opt/airflow/data/source/data.xlsx"
TABLES = [
    "users",
    "projects",
    "businesspartners",
    "projecttimes"
]


def import_table(table: str) -> None:
    df = pd.read_excel(SOURCE_FILEPATH, sheet_name=table)

    df.to_sql(
        name=table,
        con=dwh.engine,
        schema=SCHEMA_NAME,
        if_exists="replace",
        index=False
    )


def import_tables():
    dwh.ensure_schema_exists()

    is_error = False
    for table in TABLES:
        try:
            import_table(table)

            logger.info(f"✅ Successfully imported {table} into {SCHEMA_NAME}.{table}")
        except Exception as e:
            is_error = True
            logger.error(f"❌ Failed to import {table}: {e}")

    if is_error:
        raise Exception(f"Failed to import {SCHEMA_NAME}")
