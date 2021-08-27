# TODO: implement this test

import pytest

from organizations.user.update import app


@pytest.fixture
def fixture_event():
    return {
        'body': {
            'first_name': 'Arwena',
            'last_name': 'Kotka',
            'email': 'kotka@arwena.pl'
        },
        'pathParameters': {
            'Id': '61269d278cec1618eff925dd'
        }
    }


@pytest.fixture
def fixture_event_not_existing(fixture_event):
    """`Update` lambda handler should update user by id"""
    fixture_event['pathParameters']['Id'] = 'not existing id'
    return fixture_event


def test_update_existing(fixture_event):
    ret = app.lambda_handler(fixture_event, '')
    assert ret['statusCode'] == 200


def test_update_not_existing(fixture_event_not_existing):
    ret = app.lambda_handler(fixture_event_not_existing, '')
    assert ret['statusCode'] == 400
