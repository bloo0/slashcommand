
import boto3
import pandas as pd

from slashcommand.common import client_connect
from datetime import date

get_today = date.today()
today = get_today.strftime("%m/%d/%y")

def viewIngress(sgid,region):
    ec2 = client_connect.client_ec2(region)
    response = ec2.describe_security_groups(GroupIds=[sgid])
    status = response.get('ResponseMetadata', {}).get('HTTPStatusCode')

    if status == 200:
        for data in response['SecurityGroups']:
            return data['IpPermissions']
    else:
        print('Unable to get response.')
