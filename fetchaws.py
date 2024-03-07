import boto3
def fetch_token(token_name):
   ssm=boto3.client('ssm', region_name='us-east-1')
   parameter=ssm.get_parameter(Name=token_name, WithDecryption =True)
   AUTH_TOKEN=parameter['Parameter']['Value']
   return AUTH_TOKEN
print(fetch_token("/Automating/Deployments/CTMS/Cyclops/Accesstoken")) 