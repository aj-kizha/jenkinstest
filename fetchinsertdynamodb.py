import requests
url = 'http://127.0.0.1:9000/api/qualitygates/project_status'
out = requests.get(url, params={'projectKey':'pythonproj'}, auth=('admin','admin1'))
#print(("project status is").center(50,'*'))
print(out.json())
