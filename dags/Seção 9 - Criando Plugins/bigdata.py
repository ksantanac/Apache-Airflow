# Domine Apache Airflow. https://www.eia.ai/
from airflow import DAG
from big_data_operator import BigDataOperator

from datetime import datetime

dag =  DAG('bigdata', description="Nossa Dag",
        schedule_interval=None, start_date=datetime(2023,3,5),
        catchup=False)

big_data = BigDataOperator(
    task_id='big_data',
    path_to_csv_file= "/opt/airflow/data/Churn.csv",
    path_to_save_file= "/opt/airflow/data/Churn.xlsx",
    file_type= "xlsx",
    dag=dag
)

big_data