import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-085a3e7a6ed6dbda3').terminate()