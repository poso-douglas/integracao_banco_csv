import pandas as pd
import pandera as pa
from sqlalchemy import create_engine
from pathlib import Path
from dotenv import load_dotenv
import os
import pandera as pa


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

def read_sql(query: str) -> pd.DataFrame:
    settings =  load_settings()
    connection = f"mssql+pymssql://{settings['db_user']}:{settings['db_pass']}@{settings['db_host']}/{settings['db_name']}"

    engine = create_engine(connection)

    with engine.connect() as conn, conn.begin():
        df = pd.read_sql(query,conn)
    
    return df



if __name__ == "__main__":
    query = "select * from Customer"
    df = read_sql(query)
    schema_customer = pa.infer_schema(df)
    with open('schemas/customer.py','w',encoding='utf-8') as arquivo:
        arquivo.write(schema_customer.to_script())
    print(df)
