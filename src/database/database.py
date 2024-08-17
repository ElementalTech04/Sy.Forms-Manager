import os
from contextlib import contextmanager

import psycopg2
from dotenv import python_dotenv

# Load environment variables from a .env file
python_dotenv()


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.db_name = os.getenv("DB_NAME")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_host = os.getenv("DB_HOST")
        self.db_port = os.getenv("DB_PORT")

    @contextmanager
    def get_connection(self):
        connection = psycopg2.connect(
            dbname=self.db_name,
            user=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port
        )
        try:
            yield connection
        finally:
            connection.close()

    def execute_query(self, query, params=None):
        """Execute a query that modifies the database (INSERT, UPDATE, DELETE)."""
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                conn.commit()

    def fetch_query(self, query, params=None):
        """Execute a query that fetches data from the database (SELECT)."""
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                result = cursor.fetchall()
        return result
