import os
import logging
import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.mysql_to_gcs import MySqlToGoogleCloudStorageOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.hooks import SSHHook
from airflow.contrib.hooks.ssh_hook import SSHHook
from airflow.contrib.operators.ssh_operator import SSHOperator


default_args = {
    'start_date': datetime(2019, 12, 11)
}

dag = DAG(dag_id='testing1',
          default_args=default_args,
          catchup=False  ) 


t1_bash = """
        echo 'Hello World'
        """

t1 = SSHOperator(
    ssh_conn_id='remote-vm-connection',
    task_id="task1",
    command=t1_bash,
    # ssh_hook=sshHook,
    dag=dag)
