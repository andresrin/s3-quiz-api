import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = [b['Name'] for b in response.get('Buckets', [])]
    return {
        'statusCode': 200,
        'body': json.dumps({'buckets': buckets})
    }
