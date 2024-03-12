import boto3
import os
JIRA_TOKEN_NAME="jira_token_devops" 
def fetch_token(token_name):
   ssm=boto3.client('ssm', region_name='us-east-1')
   parameter=ssm.get_parameter(Name=token_name, WithDecryption =True)
   AUTH_TOKEN=parameter['Parameter']['Value']
   return AUTH_TOKEN
def create_header(token_name):
   access_Token=fetch_token(token_name)
   return access_Token   

token_name=JIRA_TOKEN_NAME
a = create_header(token_name)
if a:
   print("available")
else:
   print("not ")   






