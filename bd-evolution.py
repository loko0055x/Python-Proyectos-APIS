import os
import psycopg2
import pandas as pd

POSTGRES_USER = os.getenv('POSTGRESS_USER', 'postgres')
POSTGRES_PASSWORD = os.getenv('POSTGRESS_PASS', '1234')
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = os.getenv('POSTGRESS_PORT', '5432')
POSTGRES_DB = 'evolution'

try:
    connection = psycopg2.connect(
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        database=POSTGRES_DB
    )

    query = '''
    SELECT *
    FROM "Message"
    ORDER BY "  " desc LIMIT 10;
    '''
    query = '''
    SELECT *
    FROM "Contact"
    ORDER BY "updatedAt" asc
    LIMIT 20;
    '''
    query = '''
    SELECT *
    FROM "Contact"
    WHERE "pushName" LIKE 'Ade%' LIMIT 20;;
    '''
    query = '''
    SELECT *
    FROM "Contact"
    WHERE "pushName" LIKE 'Ma%' LIMIT 20;;
    '''

    df = pd.read_sql_query(query, connection)

    json_result = df.to_json(orient='records', force_ascii=False)
    print(json_result)

except Exception as e:
    print(f"Error al conectar o consultar: {e}")

finally:
    if 'connection' in locals() and connection:
        connection.close()
