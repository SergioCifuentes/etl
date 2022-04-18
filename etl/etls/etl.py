import numpy as np
import pandas as pd
## set the connection to the db
import sqlalchemy
import pymysql
from .sql import commands

import psycopg2
from .models import Conection
import etl as etl

def get_dataframe(file, separacion = ','):
    return pd.read_csv("."+file, sep = separacion)

def loadPostgres(conection):
    pass

def createTablesPostgres(conection: Conection):
    conn = psycopg2.connect("host="+conection.host+" dbname="+conection.databaseName+
                            " user="+conection.user+" password="+conection.password+
                            " port="+str(conection.port))
    cur = conn.cursor()
    print(commands)
    for command in commands:
        cur.execute(command)
        # close communication with the PostgreSQL database server
    cur.close()
        # commit the changes
    conn.commit()
        
def start(conection: Conection,file):
    print()

    
    createTablesPostgres(conection)
    data_frame=get_dataframe(file)
    print(conection.name)
    print(data_frame)
    pass
# example_df = pd.read_csv('Data/Clinic_Group_Practice_Reassignment_A-D.csv')
# example_df.head(6)
# dtype_pd = pd.DataFrame(example_df.dtypes, columns = ['data_type']).reset_index()
# unique_records = pd.DataFrame(example_df.nunique(), columns = ['unique_records']).reset_index()
# info_df = pd.merge(dtype_pd, unique_records, on = 'index')
# info_df

# sql_table_name= 'provider'
# initial_sql = "CREATE TABLE IF NOT EXISTS " +str(sql_table_name)+ "(key_pk INT AUTO_INCREMENT PRIMARY KEY"
