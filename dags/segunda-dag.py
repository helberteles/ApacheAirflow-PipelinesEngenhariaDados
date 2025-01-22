#Modulos
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator

#Dag
dag = DAG('segunda-dag'
	,description='Segunda DAG'
	,schedule_interval=None
	,start_date=datetime(2024, 11,30)
	,catchup=False
)


#Tasks
task1 = BashOperator(task_id="tsk1", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="tsk2", bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id="tsk3", bash_command="sleep 5", dag=dag)

#Precedencia Execucao
task1 >> [task2, task3]