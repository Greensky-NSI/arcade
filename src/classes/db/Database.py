import sqlite3

from src.utils.enums import DatabaseTables


class Database:
    """
    Classe pour gérer la base de données SQLite.

    Attributs:
        file_path (str): Le chemin du fichier de la base de données.
    """
    file_path: str

    def __init__(self, *, file_path = "src/db/database.db"):
        """
        Initialise une nouvelle instance de la classe Database.

        :param file_path: Le chemin du fichier de la base de données.
        """
        self.file_path = file_path

    def connect(self):
        """
        Établit une connexion à la base de données SQLite.

        :return: Un objet de connexion SQLite.
        """
        return sqlite3.connect(self.file_path)

    def build(self):
        """
        Crée les tables nécessaires dans la base de données si elles n'existent pas.

        :return: None
        """
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(f"CREATE TABLE IF NOT EXISTS {DatabaseTables.scores} ( score INTEGER, type INTEGER NOT NULL PRIMARY KEY)")

        conn.commit()
        conn.close()