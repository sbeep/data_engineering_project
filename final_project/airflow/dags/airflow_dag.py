from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'Sourav Saha',
    'start_date': days_ago(1) # make start date in the past
}

dag = DAG(
    dag_id="airflow_dag",
    default_args=args,
    schedule_interval="@daily",
    catchup=False
) 

with dag:
    ingest_drivers = BashOperator(
        task_id="ingest_drivers_task",
        bash_command='python3 /opt/airflow/dags/ingest_drivers.py',
        dag=dag
    )

    gcs_to_bq_drivers = BashOperator(
        task_id="gcs_to_bq_drivers_task",
        bash_command='python3 /opt/airflow/dags/gcs_to_bq_drivers.py',
        dag=dag
    )

    ingest_drivers >> gcs_to_bq_drivers 
