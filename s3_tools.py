#!/usr/bin/env python

from boto.s3.connection import S3Connection
import argparse


def process(args):
    args = vars(args)

    conn = S3Connection()
    bucket = conn.get_bucket(args['bucket'])
    key = bucket.get_key(args['key'])
    url = key.generate_url(args['timeout'])

    print(url)

if __name__ == "__main__":
    """
    Grabs a signed url for a given bucket
    """
    parser = argparse.ArgumentParser(description="Upload and get signed urls for S3 buckets")
    #parser.add_argument("action", help="action name, can be either 'get_signed_url' or 'store' ")

    parser.add_argument("--timeout", default=300, type=int , help="seconds the url should be available")
    parser.add_argument("--bucket", type=str, help="bucket name")
    parser.add_argument("--key", type=str, help="key name")


    args = parser.parse_args()

    process(args)
    

# ./s3_tools.py get_signed_url --bucket myrepo.s3.muanis --key /my_path/myfile --timeout 300
