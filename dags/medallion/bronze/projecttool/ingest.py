import pandas as pd

from sqlalchemy import text
from common.utils import dwh


SCHEMA_NAME = "projecttool"
SOURCE_FILEPATH = "/opt/airflow/data/source/data.xlsx"
TABLES = [
    "users",
    "projects",
    "businesspartners",
    "projecttimes"
]


def ensure_schema_exists():
    with dwh.engine.begin() as conn:  # ✅ Correct: Automatically commits
        conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA_NAME}"))


def import_tables():
    ensure_schema_exists()  # Ensure schema exists before writing data

    is_error = False
    for table in TABLES:
        try:
            # Read data from Excel sheet
            df = pd.read_excel(SOURCE_FILEPATH, sheet_name=table)

            # Write DataFrame to PostgreSQL in schema "projecttool.{table}"
            df.to_sql(
                name=table,
                con=dwh.engine,
                schema=SCHEMA_NAME,
                if_exists="replace",
                index=False
            )

            print(f"✅ Successfully imported {table} into {SCHEMA_NAME}.{table}")

        except Exception as e:
            is_error = True
            print(f"❌ Failed to import {table}: {e}")

    if is_error:
        raise Exception(f"Failed to import {SCHEMA_NAME}")
