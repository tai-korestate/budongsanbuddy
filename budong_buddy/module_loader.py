#!/usr/bin/python
from subprocess import call

try:
    import boto3

except:
    try:
        call(['pip install boto3'])
    
    except:
        print "AWS shell Error.  S3 services will not work."
