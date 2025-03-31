# Explore Airflow

## DAG Architecture

### Master DAG

![Master DAG](./resources/architecture/01%20Master%20DAG.png)

### Bronze Layer

![Bronze Master DAG](./resources/architecture/02%20Bronze%20Master%20DAG.png)


![Bronze PT Import DAG](./resources/architecture/03%20Bronze%20PT%20Import%20DAG.png)

### Silver Layer

![Silver Master DAG](./resources/architecture/04%20Silver%20Master%20DAG.png)

![Silver PT Transoformations DAG](./resources/architecture/05%20Silver%20Transformations%20DAG.png)

### Gold Layer

![Gold Master DAG](./resources/architecture/06%20Gold%20Master%20DAG.png)

![Gold Materialization DAG](./resources/architecture/07%20Gold%20Materialization%20DAG.png)
