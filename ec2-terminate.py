import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-044a0589204051bde').terminate() # put your instance id