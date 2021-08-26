import pytest

from organizations.user.create import app


@pytest.fixture
def fixture_event():
    return {
        'body': {
            'first_name': 'Albert',
            'last_name': 'Kot',
            'email': 'kot@albert.pl',
            'password': 'D@jJesc!!'
        }
    }


def test_create_user(fixture_event):
    """`Create` lambda handler should insert data"""
    ret = app.lambda_handler(fixture_event, '')
    assert ret['statusCode'] == 201
