import boto3
import os 
def fetch_token(token_name):
   ssm=boto3.client('ssm', region_name='us-east-1')
   parameter=ssm.get_parameter(Name=token_name, WithDecryption =True)
   AUTH_TOKEN=parameter['Parameter']['Value']
   print(AUTH_TOKEN)
a= os.environ.get('cyclops')
b=os.environ.get('Access_Token')
print(a,b)  
fetch_token("jira_token_devops")
print(fetch_token("jira_token_devops"))
print(fetch_token("/Automating/Deployments/CTMS/Cyclops/Accesstoken"))


