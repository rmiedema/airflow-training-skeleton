#!/usr/bin/env python
# coding: utf-8

# In[18]:


import airflow
from datetime import datetime
from datetime import timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BranchPythonOperator


# In[19]:


def _get_weekday(execution_date, **context):
    return execution_date.strfstime("%a")


# In[20]:


args = {
    'owner': 'R_Miedema',
    'depends_on_past': False,
    'start_date': datetime(2020, 1, 1),
    'email': ['rmiedema@bol.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}


# In[21]:


dag = DAG(
    dag_id='miedema_exercise_V',
    default_args=args,
    schedule_interval= None,
    dagrun_timeout=timedelta(minutes=5),
)

task_1 = DummyOperator(
    task_id='run_this_first',
    dag = dag,
)

task_2 = DummyOperator(
    task_id='run_this_second',
    dag = dag,
)

branching = BranchPythonOperator(
        task_id="branching", 
        python_callable=_get_weekday, 
        provide_context=True,
        dag=dag,
)

days = ["Mon","Wed","Fri"]
for day in days:
    if day = "Mon":
        branching >> DummyOperator(task_id= "Email Bob", dag=dag)
    if day = "Wed":
        branching >> DummyOperator(task_id= "Email Bert", dag=dag)
    if day = "Fri":
        branching >> DummyOperator(task_id= "Email Jan", dag=dag)

join = DummyOperator(
    task_id="final_task",
    trigger_rule = "none_failed",
    dag=dag,
)

task_1 >> task_2 >> branching >> join




