import boto3
import collections
import datetime
import sys
import pprint

def lambda_handler(event, context):
    print("Connecting to RDS...")
    client = boto3.client('rds')
    
    instances = client.describe_db_instances()['DBInstances']
    
    for instance in instances:
    
        print("RDS snapshot backups stated at %s...\n" % datetime.datetime.now())
    
        client.create_db_snapshot (
            DBInstanceIdentifier=instance['DBInstanceIdentifier'],
            DBSnapshotIdentifier='%s-%s' % (instance['DBInstanceIdentifier'],datetime.datetime.now().strftime("%Y-%m-%d"), + "-Preserve-5years"),
            Tags=[
                {
                'Key': 'Preserve',
                'Value': '5years'
                },
            ]
    
        )