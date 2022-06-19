# Make get calls to NVD API to retrieve vulnerability data
import requests
import json

# api-endpoint
URL = "https://services.nvd.nist.gov/rest/json/cves/1.0/"

# r = requests.get(url=URL)
# response = r.status_code
# print(response)

response = requests.get(URL)
dic = json.loads(response)
json_obj = json.dumps(dic, indent=2)

with open("out/output.txt", "w") as f:
   f.write(json_obj)



