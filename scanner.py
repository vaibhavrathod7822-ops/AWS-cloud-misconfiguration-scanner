import boto3
from botocore.exceptions import ClientError


def get_s3_client():
    return boto3.client("s3")


def list_buckets(s3):
    response = s3.list_buckets()
    return response["Buckets"]


def check_public_access_block(s3, bucket_name):
    try:
        response = s3.get_public_access_block(Bucket=bucket_name)
        config = response["PublicAccessBlockConfiguration"]

        if all(config.values()):
            return "PASS: Public Access Block is enabled"

        return "WARNING: Public Access Block is not fully enabled"

    except ClientError:
        return "WARNING: Public Access Block is not configured"


def check_encryption(s3, bucket_name):
    try:
        response = s3.get_bucket_encryption(Bucket=bucket_name)
        rules = response["ServerSideEncryptionConfiguration"]["Rules"]

        if rules:
            return "PASS: Default encryption is enabled"

        return "WARNING: Default encryption is not configured"

    except ClientError:
        return "WARNING: Default encryption is not configured"


def check_versioning(s3, bucket_name):
    try:
        response = s3.get_bucket_versioning(Bucket=bucket_name)
        status = response.get("Status")

        if status == "Enabled":
            return "PASS: Versioning is enabled"

        return "WARNING: Versioning is not enabled"

    except ClientError:
        return "WARNING: Versioning could not be checked"


if __name__ == "__main__":
    s3 = get_s3_client()

    for bucket in list_buckets(s3):
        name = bucket["Name"]

        public_result = check_public_access_block(s3, name)
        encryption_result = check_encryption(s3, name)
        versioning_result = check_versioning(s3, name)

        print(f"Bucket: {name}")
        print(f"  Public Access: {public_result}")
        print(f"  Encryption: {encryption_result}")
        print(f"  Versioning: {versioning_result}")
