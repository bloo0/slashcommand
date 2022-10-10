
import boto3

from slashcommand.common import client_connect
from datetime import date

get_today = date.today()
today = get_today.strftime("%m/%d/%y")

def vpnAdd(CidrIp,sgid,region):
    ec2 = client_connect.rclient_ec2(region)
    secgroup = ec2.SecurityGroup(sgid)
    response = secgroup.authorize_ingress(
        IpPermissions=[
            {
                'FromPort': 1194,
                'IpProtocol': 'udp',
                'IpRanges': [
                    {
                        'CidrIp': CidrIp,
                        'Description': today
                    }
                ],
                'ToPort': 1194
            }
        ])

    status = response.get('ResponseMetadata', {}).get('HTTPStatusCode')

    if status == 200:
        return f'{CidrIp} added successfully.'
    else:
        print('Unable to get response.')
    

def sshAdd(CidrIp,sgid,region):
    ec2 = client_connect.client_ec2(region)
    secgroup = ec2.SecurityGroup(sgid)
    response = secgroup.authorize_ingress(
        IpPermissions=[
            {
                'FromPort': 22,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': CidrIp,
                        'Description': '' # TODO: current date
                    }
                ],
                'ToPort': 22,
            }
        ])