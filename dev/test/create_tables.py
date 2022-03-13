"""
Create the Music and User tables

This is intended to be used within a continuous integration test.
As such, it presumes that it is creating the tables in a local
DynamoDB instance.

It may work with the full AWS DynamoDB service but it has
not been tested on that.
"""

# Standard libraries

# Installed packages
import boto3

# Local modules

class DB_Manager:
    def __init__(self, url, region, access_key_id, secret_access_key):
        self.url = url
        self.region = region
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key
        
        self.dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url=url,
            region_name=region,
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key)
        
    def create_table(self, tbl_name, key="id"):
        tbl = self.dynamodb.create_table(
            TableName=tbl_name,
            AttributeDefinitions=[{
                "AttributeName": key, "AttributeType": "S"}],
            KeySchema=[{"AttributeName": key, "KeyType": "HASH"}],
            ProvisionedThroughput={
                "ReadCapacityUnits": 5, "WriteCapacityUnits": 5}
        )
        tbl.wait_until_exists()        
