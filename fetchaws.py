import boto3
import os 
def fetch_token(token_name):
   ssm=boto3.client('ssm', region_name='us-east-1')
   parameter=ssm.get_parameter(Name=token_name, WithDecryption =True)
   AUTH_TOKEN=parameter['Parameter']['Value']
   return AUTH_TOKEN
# a= os.environ.get('cyclops')
b="jira_token_devops"
if fetch_token(b):
   print("token found")
else:
   print("token found")





