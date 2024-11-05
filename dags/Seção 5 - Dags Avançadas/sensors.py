# Domine Apache Airflow. https://www.eia.ai/
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.http.sensors.http import HttpSensor

from datetime import datetime

import requests

dag =  DAG('httpSensor', description="httpSensor",
        schedule_interval=None,start_date=datetime(2023,3,5),
        catchup=False)

def query_api():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    print(response.text)


check_api = HttpSensor(
    task_id="check_api",
    http_conn_id="connection",
    endpoint="random",
    poke_interval=5,
    timeout=20,
    dag=dag
)

process_data = PythonOperator(
    task_id='process_data', 
    python_callable=query_api, 
    dag=dag
)

check_api >> process_data

