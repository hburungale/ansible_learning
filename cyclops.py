import requests
import os
# cyclops_template = os.environ.get('TEMPLATE')
# CTMS_URL = os.environ.get('CTMS_URL')
# S3 =os.environ.get('S3')
if S3 == "red":
    cyclops_url = "https://cyclopsui.imedidata.com/"
else:
    cyclops_url = "https://cyclopsui-sandbox.imedidata.net"
    url = f"{cyclops_url}/api/v0/url-configurations/CTMS/{CTMS_DIstro}/{CTMS_URL}"
    payload = {}
    headers = {
        'Access-Token': os.environ.get('cyclops'), #stored in secure variables, will be adding in secrete manager after testing
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, data=payload)
    if response.status_code == 200:
        json_dict = response.json()
        print(json_dict)
    else:
        print(f"Error: {response.status_code} - {response.text}")
        