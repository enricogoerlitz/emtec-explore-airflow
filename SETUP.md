# Airflow Local Setup Guide

This guide provides step-by-step instructions to set up Apache Airflow locally using Docker Compose.

## Prerequisites

Ensure the following tools are installed on your system:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Step 1: Download the Official `docker-compose.yaml`

Download the official `docker-compose.yaml` file for Apache Airflow:

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.5/docker-compose.yaml'
```

## Step 2: Create Required Directories

Create the necessary directories for Airflow to store DAGs, logs, plugins, and configuration files:

```bash
mkdir -p ./dags ./logs ./plugins ./config
```

## Step 3: Set Up the Airflow User

Create an `.env` file to define the Airflow user ID. This ensures proper permissions for the Airflow containers:

```bash
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

## Step 4: Initialize the Airflow Database

Run the following command to initialize the Airflow database. This step sets up the backend database used by Airflow:

```bash
docker compose up airflow-init
```

## Step 5: Start All Airflow Services

Once the initialization is complete, start all Airflow services in detached mode:

```bash
docker compose up -d
```

## Step 6: Install Additional Python Dependencies (Optional)

If your DAGs require additional Python dependencies, install them using the following commands:

```bash
docker compose exec airflow-worker python -m pip install -r /opt/airflow/config/requirements.txt
docker compose exec airflow-scheduler python -m pip install -r /opt/airflow/config/requirements.txt
```

## Step 7: Access the Airflow Web Interface

Once the services are running, access the Airflow web interface at:

[http://localhost:8080/home](http://localhost:8080/home)

Use the following credentials to log in:

- **Username**: `airflow`
- **Password**: `airflow`

## Step 8: Add a Postgres Connection

To connect Airflow to a Postgres database, follow these steps:

1. Navigate to **Admin > Connections** in the Airflow web interface.
2. Click on **+** to create a new connection.
3. Fill in the connection details for your Postgres database.

## Step 9: Create a Schema in Postgres

Run the following SQL command in your Postgres database to create a schema for your data warehouse:

```sql
CREATE SCHEMA gold_pr;
```

## Step 10: Trigger a DAG via API

You can trigger a DAG run programmatically using the Airflow REST API. Use the following example to trigger the `master_dag` DAG:

### API Request

**Endpoint**: `POST http://localhost:8080/api/v1/dags/master_dag/dagRuns`

**Request Body**:

```json
{
    "dag_run_id": "run_via_api_1",
    "logical_date": "2025-03-20T00:00:00Z"
}
```

**Authentication**: Use Basic Authentication with the following credentials:

- **Username**: `airflow`
- **Password**: `airflow`

## Step 11: Check DAG Run Status

To check the status of a DAG run, use the `GET` method with the `dag_run_id` in the API. Refer to the Airflow API documentation for more details.

## Notes

- Ensure that all required services (e.g., `airflow-webserver`, `airflow-scheduler`, `airflow-worker`) are running before triggering DAGs.
- For troubleshooting, check the logs using the following command:

```bash
docker compose logs -f
```

This concludes the setup guide for Apache Airflow. You are now ready to create and manage your workflows locally!