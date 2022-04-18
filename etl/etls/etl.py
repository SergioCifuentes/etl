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
   
def create_person(row, data_frame  : pd.DataFrame,conection: Conection):
    conn = psycopg2.connect("host="+conection.host+" dbname="+conection.databaseName+
                            " user="+conection.user+" password="+conection.password+
                            " port="+str(conection.port))
    cur = conn.cursor()
    cur.execute("SELECT ID_PERSONA FROM REP_PERSONA WHERE DPI = '%s'", (row['dpi'],))
    genero=True
    if row['genero']=='M':
        genero=True

    if cur.fetchone() is None:
        cur.execute("INSERT INTO REP_PERSONA(DPI,PRIMER_NOMBRE,SEGUNDO_NOMBRE,PRIMER_APELLIDO,"+
        "SEGUNDO_APELLIDO,APELLIDO_CASADA,ORDEN_CEDULA ,REGISTRO_DEDULA ,DIRECCION_RESIDENCIA ,"+
        "NIT,GENERO,TELEFONO,CORREO_ELECTRONICO ,FECHA_NACIMIENTO) VALUES('%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (row['dpi'],row['primer_nombre'],row['segundo_nombre'],row['primer_apellido'],row['segundo_apellido'],
         row['apellido_casada'],row['cedula_orden'],row['cedula_registro'],row['direccion_residencia'],
         row['nit'],genero,row['telefono'],row['correo_electronico'],'1999-09-09'))
    cur.close()
    conn.commit()
    
def create_company(row, data_frame  : pd.DataFrame,conection: Conection):
    conn = psycopg2.connect("host="+conection.host+" dbname="+conection.databaseName+
                            " user="+conection.user+" password="+conection.password+
                            " port="+str(conection.port))
    cur = conn.cursor()
    cur.execute("SELECT ID_EMPRESA FROM REP_EMPRESA WHERE NIT = %s", (row['nit_empresa'],))

    if cur.fetchone() is None:
        cur.execute("INSERT INTO REP_EMPRESA(NOMBRE_EMPRESA,NIT,CODIGO,DIRECCION,"+
        "TELEFONO) VALUES(%s,%s,%s,%s,%s)",
        (row['nombre_empresa'],row['nit_empresa'],row['codigo_unico_empresa'],row['direccion_empresa'],row['telefono_empresa']))
    cur.close()
    conn.commit()
    

    
def create_job(row, data_frame  : pd.DataFrame,conection: Conection):
    conn = psycopg2.connect("host="+conection.host+" dbname="+conection.databaseName+
                            " user="+conection.user+" password="+conection.password+
                            " port="+str(conection.port))
    cur = conn.cursor()
    cur.execute("SELECT ID_EMPRESA FROM REP_EMPRESA WHERE NIT = %s", (row['nit_empresa'],))
    id_empresa=cur.fetchone()[0] 
    cur.execute("SELECT ID_PERSONA FROM REP_PERSONA WHERE DPI = '%s'", (row['dpi'],))
    id_empleado=cur.fetchone()[0]                                                                                                       
    cur.execute("SELECT ID_TRABAJO FROM REP_TRABAJO WHERE ID_PERSONA = %s AND ID_EMPRESA = %s", (id_empleado,id_empresa))

    if cur.fetchone() is None:
        cur.execute("INSERT INTO REP_TRABAJO(ID_PERSONA,FECHA_INICIAL,FECHA_FINAL,ID_EMPRESA,NOMBRE_PUESTO,MES_PLANILLA,SALARIO)"+
        " VALUES(%s,%s,%s,%s,%s,%s,%s)",
        (id_empleado,'2010-09-09','2020-10-10',id_empresa,row['departamento_trabajo'],row['municipio_trabajo'],float(row['salario'].replace(",", ""))))
    cur.close()
    conn.commit()     
        
def start(conection: Conection,file):
    conn = psycopg2.connect("host="+conection.host+" dbname="+conection.databaseName+
                            " user="+conection.user+" password="+conection.password+
                            " port="+str(conection.port))
    cur = conn.cursor()
    createTablesPostgres(conection)
    data_frame=get_dataframe(file)
    print(conection.name)
    print(data_frame)
    for index, row in data_frame.iterrows():
        create_person(row,data_frame,conection)
        create_company(row,data_frame,conection)
        create_job(row,data_frame,conection)
        
         
    
# example_df = pd.read_csv('Data/Clinic_Group_Practice_Reassignment_A-D.csv')
# example_df.head(6)
# dtype_pd = pd.DataFrame(example_df.dtypes, columns = ['data_type']).reset_index()
# unique_records = pd.DataFrame(example_df.nunique(), columns = ['unique_records']).reset_index()
# info_df = pd.merge(dtype_pd, unique_records, on = 'index')
# info_df

# sql_table_name= 'provider'
# initial_sql = "CREATE TABLE IF NOT EXISTS " +str(sql_table_name)+ "(key_pk INT AUTO_INCREMENT PRIMARY KEY"
