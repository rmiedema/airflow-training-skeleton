#!/usr/bin/env python
# coding: utf-8

# In[30]:


import airflow
from datetime import datetime
from datetime import timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

args = {
    'owner': 'R_Miedema',
    'depends_on_past': False,
    'start_date': datetime(2020, 1, 1),
    'email': ['rmiedema@bol.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    dag_id='miedema_test',
    default_args=args,
    schedule_interval= '@daily',
    dagrun_timeout=timedelta(minutes=60),
)

t1 = DummyOperator(
    task_id='task1',
    dag=dag,
)

t2 = DummyOperator(
    task_id='task2',
    dag=dag,
)

t3 = DummyOperator(
    task_id='task3',
    dag=dag,
)

t4 = DummyOperator(
    task_id='task4',
    dag=dag,
)

t5 = DummyOperator(
    task_id='task5',
    dag=dag,
)

t1 >> t2 >> t3 >> t5
t2 >> t4 >> t5

