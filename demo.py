from moto import mock_aws
import boto3

from scanner import (
    list_buckets,
    check_public_access_block,
    check_encryption,
    check_versioning
)


@mock_aws
def run_demo():
    s3 = boto3.client("s3", region_name="us-east-1")

    # Create test buckets
    s3.create_bucket(Bucket="demo-bucket-1")
    s3.create_bucket(Bucket="demo-bucket-2")

    print("=" * 50)
    print("AWS CLOUD MISCONFIGURATION SCANNER")
    print("=" * 50)

    buckets = list_buckets(s3)

    for bucket in buckets:
        name = bucket["Name"]

        public_result = check_public_access_block(s3, name)
        encryption_result = check_encryption(s3, name)
        versioning_result = check_versioning(s3, name)

        print(f"\nBucket: {name}")
        print(f"  Public Access : {public_result}")
        print(f"  Encryption    : {encryption_result}")
        print(f"  Versioning    : {versioning_result}")

    print("\n" + "=" * 50)
    print("SCAN COMPLETED SUCCESSFULLY")
    print("=" * 50)


if __name__ == "__main__":
    run_demo()
