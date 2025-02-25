import os
from django.conf import settings

import sqlite3
con = sqlite3.connect("tutorial.db")

# DB_NAME = os.getenv('DB_NAME')
# DB_USERNAME = os.getenv('DB_USERNAME')
# DB_PASSWORD = os.getenv('DB_PASSWORD')

__all__ = ["DbConnect"]

class DbConnect:
    def __init__(self) -> None:
        db = settings.DATABASES['default']['NAME']
        self.conn = sqlite3.connect(db)
        self.conn.row_factory = self.dict_factory
        self.cur = self.conn.cursor()
        # self.conn = psycopg2.connect(f"dbname='{DB_NAME}' user='{DB_USERNAME}' host='pgsql' password='{DB_PASSWORD}'")
        # self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def dict_factory(self, cursor, row):
        fields = [column[0] for column in cursor.description]
        return {key: value for key, value in zip(fields, row)}
