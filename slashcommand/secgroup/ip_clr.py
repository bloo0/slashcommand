import boto3
import pandas as pd

from slashcommand.common import client_connect

def cleanIngress(sgid,region):
    ec2 = client_connect.rclient_ec2(region)
    secgroup = ec2.SecurityGroup(sgid)
    response = secgroup.revoke_ingress(IpPermissions=secgroup.ip_permissions)

    status = response.get('ResponseMetadata', {}).get('HTTPStatusCode')

    if status == 200:
        return f'Ingress revoked'
    else:
        print('Unable to get response.')

