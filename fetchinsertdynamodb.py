import requests
import json
import boto3

url = 'http://127.0.0.1:9000/api/qualitygates/project_status'
out = requests.get(url, params={'projectKey': 'pythonproj'},
                   auth=('admin', 'admin1'))

records = {}
records['projectid'] = 'pythonproj'
records['condition'] = out.json()['projectStatus']['conditions']

dynamodb = boto3.resource('dynamodb', region_name="ap-south-1")
table = dynamodb.Table('projectquality')
table.put_item(Item=records)
