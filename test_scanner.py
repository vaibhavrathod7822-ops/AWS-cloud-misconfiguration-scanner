from moto import mock_aws
import boto3

from scanner import (
    list_buckets,
    check_public_access_block,
    check_encryption,
    check_versioning,
)


@mock_aws
def test_scanner():
    s3 = boto3.client("s3", region_name="us-east-1")

    s3.create_bucket(Bucket="test-bucket-1")
    s3.create_bucket(Bucket="test-bucket-2")

    buckets = list_buckets(s3)

    names = [bucket["Name"] for bucket in buckets]

    assert "test-bucket-1" in names
    assert "test-bucket-2" in names

    public_result = check_public_access_block(s3, "test-bucket-1")
    encryption_result = check_encryption(s3, "test-bucket-1")
    versioning_result = check_versioning(s3, "test-bucket-1")

    assert public_result == "WARNING: Public Access Block is not configured"
    assert encryption_result == "WARNING: Default encryption is not configured"
    assert versioning_result == "WARNING: Versioning is not enabled"

    print("Scanner test passed!")


if __name__ == "__main__":
    test_scanner()
