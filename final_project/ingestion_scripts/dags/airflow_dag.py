from datetime import datetime
from airflow import DAG
from airflow.operators import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import ingest_drivers
import gcs_to_bq_drivers

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
    ingest_drivers = PythonOperator(
        task_id="ingest_drivers_task",
        python_callable=ingest_drivers.main,
        dag=dag
    )

    gcs_to_bq_drivers = PythonOperator(
        task_id="gcs_to_bq_drivers_task",
        python_callable=gcs_to_bq_drivers.main,
        dag=dag
    )

    ingest_drivers >> gcs_to_bq_drivers 