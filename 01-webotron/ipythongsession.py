# coding: utf-8
import boto3
session = boto.Session(profile_name='bronson')
session = boto3.Session(profile_name='bronson')
s3 = session.resorce('s3')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
get_ipython().run_line_magic('history', '')
