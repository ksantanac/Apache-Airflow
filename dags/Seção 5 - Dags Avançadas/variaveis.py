from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable

from datetime import datetime

dag =  DAG('variaveis', description="variaveis",
        schedule_interval=None,start_date=datetime(2024,8,26),
        catchup=False)

def print_variable(**context):
    minha_Var = Variable.get("minhavar")
    print(f"O valor da variável é: {minha_Var}")

task1 = PythonOperator(task_id="tsk1", python_callable=print_variable, dag=dag)

task1