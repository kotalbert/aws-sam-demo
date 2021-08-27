import pymongo
import pytest

from organizations.user.create.app import lambda_handler as create_lambda_handler
from organizations.user.delete.app import lambda_handler as delete_lambda_handler
from organizations.user.utils.db import MongoDBConnection


@pytest.fixture
def fixture_event_create():
    return {
        'body': {
            'first_name': 'to-be-deleted',
            'last_name': 'to-be-deleted',
            'email': 'kot@albert.pl',
            'password': 'D@jJesc!!'
        }
    }


@pytest.fixture
def fixture_event_delete():
    with MongoDBConnection() as mongo:
        connection = mongo.connection.get_database()['registrations']
        last_inserted_id = connection.find_one({}, sort=[('_id', pymongo.DESCENDING)])
    return {
        'pathParameters': {
            'Id': last_inserted_id
        }
    }


@pytest.fixture
def fixture_non_existing_delete():
    return {
        'pathParameters': {
            'Id': 'not-existing-id'
        }
    }


def test_delete_by_id(fixture_event_create):
    create_res = create_lambda_handler(fixture_event_create, '')
    assert create_res['statusCode'] == 201

    delete_res = delete_lambda_handler(fixture_event_delete, '')
    assert delete_res['statusCode'] == 204


def test_delete_not_existing(fixture_non_existing_delete):
    res = delete_lambda_handler(fixture_non_existing_delete, '')
    assert res['statusCode'] == 400
