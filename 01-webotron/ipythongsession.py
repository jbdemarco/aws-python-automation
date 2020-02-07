import boto3
session = boto3.Session(profile_name='bronson')
s3 = session.resource('s3')
    
