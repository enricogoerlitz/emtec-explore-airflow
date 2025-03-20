

```bash
# Download the official docker-compose.yaml
$ curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.5/docker-compose.yaml'

# Create the required directories
$ mkdir -p ./dags ./logs ./plugins ./config

# Initialize the environment with the correct Airflow user
$ echo -e "AIRFLOW_UID=$(id -u)" > .env

# Initialize the database (this step is crucial)
$ docker-compose up airflow-init
$ docker compose up airflow-init

# Once initialization is complete, start all services
$ docker-compose up -d
$ docker compose up -d

$ docker compose exec airflow-worker python -m pip install -r /opt/airflow/config/requirements.txt
$ docker compose exec airflow-scheduler python -m pip install -r /opt/airflow/config/requirements.txt
```

Link: (http://localhost:8080/home)[http://localhost:8080/home]
username: airflow
password: airflow

Add postgres connection: Admin > Connection > new connection

CREATE SCHEMA gold_pr;


### API Call:

POST http://localhost:8080/api/v1/dags/master_dag/dagRuns
{
    "dag_run_id": "run_via_api_1",
    "logical_date": "2025-03-20T00:00:00Z"
}
Basic-Auth: airflow + airflow

- mit GET und dag_run_id kann man dann auch status abfragen