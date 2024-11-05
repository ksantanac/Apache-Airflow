from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import datetime

dag = DAG(
    'segunda_dag',
    description="Segunda DAG",
    schedule_interval=None,
    start_date=datetime(2024,8,19),
    catchup=False
)

task1 = BashOperator(task_id="tsk1", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="tsk2", bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id="tsk3", bash_command="sleep 5", dag=dag)

task1 >> [task2, task3]