# AWS Cloud Misconfiguration Scanner

A Python-based AWS S3 security scanner that detects common cloud misconfigurations related to public access, encryption, and bucket versioning.

## Features

- Detects S3 buckets
- Checks Public Access Block configuration
- Checks default server-side encryption
- Checks bucket versioning
- Reports security warnings
- Includes automated tests using Moto
- Includes a local working demo without requiring real AWS credentials

## Requirements

- Python 3
- boto3
- moto[s3]

## Installation

```bash
pip install -r requirements.txt
