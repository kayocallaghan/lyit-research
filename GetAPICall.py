# Make get calls to NVD API to retrieve vulnerability data
import requests

# api-endpoint
URL = "https://services.nvd.nist.gov/rest/json/cves/1.0/"

r = requests.get(url=URL)
response = r.status_code
print(response)



