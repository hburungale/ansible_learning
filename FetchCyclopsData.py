import requests
import json
import boto3
import os

def get_json_data():
    token_name = "gocd_stage_token"
    ssm = boto3.client('ssm', region_name='us-east-1')
    parameter = ssm.get_parameter(Name=token_name)
    BEARER_TOKEN = parameter['Parameter']['Value']
    url = "https://cyclopsui-sandbox.imedidata.net/api/v0/url-configurations/CTMS/CTMS_DIstro/test_url.net"

    payload = {}
    headers = {
        'Access-Token': os.environ.get('cyclops'),
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers, data=payload)

    if response.status_code == 200:
        json_dict = response.json()
        return json_dict
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

