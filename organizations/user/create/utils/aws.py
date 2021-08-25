import json

import boto3


def get_db_credentials():
    secret_name = "aws-sam-db-secret"
    region_name = "eu-central-1"

    # Create a Secrets Manager client
    session = boto3.Session(profile_name='aws-sam')
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    secret_value_str = client.get_secret_value(SecretId=secret_name)['SecretString']
    return json.loads(secret_value_str)


def main():
    secret_dict = get_db_credentials()
    assert secret_dict['username'] == 'aws-sam-user'


if __name__ == '__main__':
    main()
