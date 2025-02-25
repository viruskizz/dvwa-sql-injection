import os
import psycopg2
from psycopg2.extras import RealDictCursor

DB_NAME = os.getenv('DB_NAME')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')

__all__ = ["DbConnect"]

class DbConnect:
    def __init__(self) -> None:
        self.conn = psycopg2.connect(f"dbname='{DB_NAME}' user='{DB_USERNAME}' host='pgsql' password='{DB_PASSWORD}'")
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

