import boto3
import argparse
import os
from urllib.parse import urlparse


def parse_s3_path(s3_path):
    o = urlparse(s3_path)
    return o.netloc, o.path


def main(args):
    bucket_name, key = parse_s3_path(args.output)

    s3 = boto3.resource(
        's3',
        aws_access_key_id=os.environ['S3_ACCESS_KEY'],
        aws_secret_access_key=os.environ['S3_SECRET_KEY'],
        endpoint_url=os.environ['S3_HOST'],
        use_ssl=False,
    )

    data = ""
    for i in range(15):
        data += f"{i}\n"

    o = s3.Object(bucket_name, key)
    result = o.put(Body=data)

    if result.get('ResponseMetadata').get('HTTPStatusCode') != 200:
        raise "file not uploaded"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=str, required=True)
    main(parser.parse_args())
