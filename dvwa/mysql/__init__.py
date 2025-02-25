import os
from MySQLdb import _mysql

DB_NAME = os.getenv('DB_NAME')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')

__all__ = ["DbConnect"]

class DbConnect:
    def __init__(self) -> None:
        self.conn = _mysql.connect(
            host="mysql",
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD
        )

