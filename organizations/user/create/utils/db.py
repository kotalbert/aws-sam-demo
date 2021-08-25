from pymongo import MongoClient

from .aws import get_db_credentials


class MongoDBConnection:
    def __init__(self):
        self.connection: MongoClient

    def __enter__(self):
        credentials = get_db_credentials()
        username = credentials['username']
        password = credentials['password']
        host = credentials['host']
        dbname = credentials['dbname']

        self.connection = MongoClient(f'mongodb+srv://{username}:{password}@{host}/{dbname}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
