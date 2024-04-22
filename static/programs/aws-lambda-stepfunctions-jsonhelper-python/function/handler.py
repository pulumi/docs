import json
import boto3

def handler(event, context):        
  print(json.dumps(event))
