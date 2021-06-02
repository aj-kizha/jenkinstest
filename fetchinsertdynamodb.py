import requests
import boto3
import sys

url = 'http://127.0.0.1:9000/api/qualitygates/project_status'
out = requests.get(url, params={'projectKey': 'pythonproj'},
                   auth=('admin', 'admin1'))

client = boto3.client(
    'dynamodb',
    aws_access_key_id=sys.argv[1],
    aws_secret_access_key=sys.argv[2],
    region_name="ap-south-1"
)

records = {}
records['projectid'] = 'pythonproj'
records['condition'] = out.json()['projectStatus']['conditions']

dynamodb = boto3.resource('dynamodb', aws_access_key_id=sys.argv[1],
                          aws_secret_access_key=sys.argv[2],
                          region_name="ap-south-1")
table = dynamodb.Table('projectquality')
table.put_item(Item=records)
