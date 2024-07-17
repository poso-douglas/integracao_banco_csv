import pandas as pd
import pandera as pa
from sqlalchemy import create_engine
from pathlib import Path
from dotenv import load_dotenv
import os
import pandera as pa
from .customer import SchemaCustomer,SchemaCustomerCSV
from datetime import datetime, timedelta
import numpy as np


def load_settings():
    """"Carrega as configurações de acesso do projeto das variaveis de ambiente"""
    path_init = Path.cwd() / '.env'
    load_dotenv(dotenv_path=path_init)

    settings = {
        "db_host": os.getenv("SQL_HOST"),
        "db_port": os.getenv("SQL_PORT"),
        "db_name": os.getenv("SQL_NAME"),
        "db_user": os.getenv("SQL_USER"),
        "db_pass": os.getenv("SQL_PASS")
    }
    return settings


@pa.check_output(SchemaCustomer)
def read_sql(query: str) -> pd.DataFrame:
    settings =  load_settings()
    connection = f"mssql+pymssql://{settings['db_user']}:{settings['db_pass']}@{settings['db_host']}/{settings['db_name']}"

    engine = create_engine(connection)

    with engine.connect() as conn, conn.begin():
        df = pd.read_sql(query,conn)
    
    return df

@pa.check_input(SchemaCustomer)
@pa.check_output(SchemaCustomerCSV)
def transform(df: pd.DataFrame):
    df["MaritalStatus"] = np.where(df["MaritalStatus"] == "S","Single","Married")
    df["Gender"] = np.where(df["Gender"] == "M","Male","Female")
    df["FullName"] = df["FirstName"] + " " + df["LastName"]
    return df


def soma_dois_numeros(n1:int, n2:int) -> int:
    return n1 + n2

if __name__ == "__main__":
    print(soma_dois_numeros("1","2"))

    # query = "select * from Customer"
    # df = read_sql(query)
    # df2 = transform(df)
    # df2.to_csv("output/Customers.csv",sep=";",header=True)

    # schema_customer = pa.infer_schema(df)
    # with open('src/customer.py','w',encoding='utf-8') as arquivo:
    #     arquivo.write(schema_customer.to_script())
    # print(df)
