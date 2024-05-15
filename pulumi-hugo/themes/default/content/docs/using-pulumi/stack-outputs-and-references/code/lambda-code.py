import json
import os
import boto3
import datetime

s3 = boto3.resource('s3')

BUCKET_NAME = os.environ['BUCKET_NAME']

def lambda_handler(event, context):
    
    current_time = str(datetime.datetime.utcnow()).replace(" ", "")
    data_string = "Hello Pulumi!"
    
    object = s3.Object(
        bucket_name=BUCKET_NAME, 
        key=f'{current_time}_test_file.txt'
    )
    
    object.put(Body=data_string)