import requests
import boto3
import sys
from datetime import datetime

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

'''Security insertion'''
securityurl = 'http://127.0.0.1:9000/api/hotspots/search'
out = requests.get(securityurl, params={'projectKey': 'pythonproj'},
                   auth=('admin', 'admin1'))
security_out = out.json()

hotspot_record = {}
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

for item in security_out['hotspots']:
    hotspot_record['projectid'] = item['project']
    hotspot_record['datetime'] = dt_string
    hotspot_record['securitycat'] = item['securityCategory']
    hotspot_record['vulnerabilityProbability'] =\
        item['vulnerabilityProbability']
    hotspot_record['component'] = item['component']
security_table = dynamodb.Table('projecthotspot')
security_table.put_item(Item=hotspot_record)
