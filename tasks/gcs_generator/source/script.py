import argparse
import os
import json
from urllib.parse import urlparse
from google.cloud import storage


def parse_s3_path(s3_path):
    o = urlparse(s3_path)
    return o.netloc, o.path.lstrip("/")

def getClient() -> storage.Client:
    creds = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", None)
    if not creds:
        raise RuntimeError("GOOGLE_APPLICATION_CREDENTIALS not set")
    try:
        credsJson = json.loads(creds)
        return storage.Client.from_service_account_info(credsJson)
    except json.decoder.JSONDecodeError:
        return storage.Client()

def main(args):
    bucket_name, key = parse_s3_path(args.output)

    storage_client = getClient()

    data = ""
    for i in range(15):
        data += f"{i}\n"

    obj = storage_client.bucket(bucket_name).blob(key)
    obj.upload_from_string(data)
    print("obj uploaded, md5_hash:", obj.md5_hash)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=str, required=True)
    main(parser.parse_args())
