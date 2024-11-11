import psycopg2
from psycopg2.extras import RealDictCursor


def get_db_connection():
    conn = psycopg2.connect(
        dbname="artesanos_db",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
    conn.set_client_encoding('UTF8')  # Configuración explícita de codificación
    return conn
