import os
from django.conf import settings

import sqlite3

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

    def dict_factory(self, cursor, row):
        fields = [column[0] for column in cursor.description]
        return {key: value for key, value in zip(fields, row)}
