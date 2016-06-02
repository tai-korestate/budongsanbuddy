import os
import boto3

media_url = './media/unknown'

target = ''
bucket_name = 'korestate'

s3 = boto3.resource('s3')

abs_curdir = os.path.abspath('.')
dir_cointents = os.path.join(abs)


def write_all(target = media_url, to_bucket = bucket_name, usr = 'images'):
    
    dir_contents = os.listdir(target)
    print "s3handler WRITING TO::: {}".format(dir_contents)   

    for f in dir_contents:
        FILE_PATH = os.path.join(target,f)
        if os.path.isfile(FILE_PATH):
            send_file = open(FILE_PATH,'rb')
            s3.Object(to_bucket, os.path.join(usr,f)).put(Body=send_file)


        else:
            pass


def flush(dir_to_flush = media_url):
    os.system('rm {}/*'.format(dir_to_flush))
