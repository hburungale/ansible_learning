import boto3

token_name = "gocd_stage_token"
ssm = boto3.client('ssm', region_name='us-east-1')
parameter = ssm.get_parameter(Name=token_name)
BEARER_TOKEN = parameter['Parameter']['Value']

if BEARER_TOKEN :
    print("yess")
else : 
    print("not found")
