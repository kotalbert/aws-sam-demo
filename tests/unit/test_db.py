from organizations.user.utils.db import MongoDBConnection


def test_connection():
    with MongoDBConnection() as con:
        assert con.connection.get_database().name == 'aws-sam-db'
