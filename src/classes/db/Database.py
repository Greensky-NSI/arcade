import sqlite3

from utils.enums import DatabaseTables


class Database:
    file_path: str

    def __init__(self, *, file_path = "src/db/database.db"):
        self.file_path = file_path

    def connect(self):
        return sqlite3.connect(self.file_path)

    def build(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(f"CREATE TABLE IF NOT EXISTS {DatabaseTables.scores} ( score INTEGER, type INTEGER NOT NULL PRIMARY KEY)")

        conn.commit()
        conn.close()