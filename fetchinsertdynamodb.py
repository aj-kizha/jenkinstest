import requests
url = 'http://127.0.0.1:9000/api/qualitygates/project_status'
out = requests.get(url, params={'projectKey': 'pythonproj'},
                   auth=('admin', 'admin1'))
print(out.json())
