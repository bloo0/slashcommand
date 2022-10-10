import boto3

def client_ec2(region):
    ec2 = boto3.client('ec2', region_name=region)
    print('client connected')
    return ec2

def rclient_ec2(region):
    ec2 = boto3.resource('ec2', region_name=region)
    print('resource connected')
    return ec2