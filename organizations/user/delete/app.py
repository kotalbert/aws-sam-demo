import json

import bson
from bson import ObjectId

from ..utils import db


def lambda_handler(event, context):
    try:
        object_id = event["pathParameters"]["Id"]
    except TypeError:
        object_id = None

    with db.MongoDBConnection() as mongo:
        collection = mongo.connection.get_database()['registrations']
        try:
            collection.delete_one({"_id": ObjectId(object_id)})
        except bson.errors.InvalidId:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "message": "Error ! Invalid ObjectId",
                    "data": None
                })
            }

        return {
            "statusCode": 204,
            "body": json.dumps({
                "message": "Data Deleted !",
                "data": None
            })
        }
