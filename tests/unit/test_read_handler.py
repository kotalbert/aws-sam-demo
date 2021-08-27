import pytest

from organizations.user.read import app


@pytest.fixture
def fixture_event():
    return {
        'pathParameters': {
            'Id': '61269d278cec1618eff925dd'
        }
    }


def test_read_users():
    """`Read` lambda handler should select all users"""
    ret = app.lambda_handler({}, '')
    assert ret['statusCode'] == 200


def test_read_user_by_id(fixture_event):
    """`Read` lambda handler should select user by id."""
    ret = app.lambda_handler(fixture_event, '')
    assert ret['statusCode'] == 200
