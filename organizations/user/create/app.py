import json

from marshmallow import ValidationError

from .utils import db, validator


def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        result = validator.UserRegistrationSchema()

        # Check if dictionary is empty.
        res = not bool(result.validate(body))

        if res:
            # Store information in DB
            with db.MongoDBConnection() as mongo:
                database = mongo.connection.get_database()
                collection = database['registrations']
                collection.insert_one(result.load(body))

            return {
                "statusCode": 201,
                "body": json.dumps({
                    "message": "Registered Successfully",
                    "data": result.validate(body)
                })
            }
        else:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Error !",
                                    "data": result.validate(body)
                                    })
            }

    except ValidationError as err:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": err.messages
            })
        }

    except KeyError:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Something went wrong. Unable to parse data !"
            })
        }
