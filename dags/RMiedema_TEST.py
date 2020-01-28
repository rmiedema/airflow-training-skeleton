#!/usr/bin/env python
# coding: utf-8

# In[12]:


import airflow
from datetime import timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator


# In[13]:


args = {
    'owner': 'R_Miedema',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
    'email': ['rmiedema@bol.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}


# In[18]:


dag = DAG(
    dag_id='miedema_test',
    default_args=args,
    schedule_interval= None,
    dagrun_timeout=timedelta(minutes=60),
)


# In[21]:


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





