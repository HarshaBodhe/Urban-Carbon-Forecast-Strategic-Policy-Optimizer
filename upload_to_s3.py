# save as upload_to_s3.py
import boto3
from botocore.exceptions import NoCredentialsError

# --- Replace with your details ---
AWS_ACCESS_KEY = " "
AWS_SECRET_KEY = " "
BUCKET_NAME = "vehicledatacapstone"
FILE_PATH = "after_optimization.csv"
S3_KEY = "raw/after_optimization.csv"

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print(f"✅ Uploaded {local_file} → s3://{bucket}/{s3_file}")
        return True
    except FileNotFoundError:
        print("❌ File not found")
        return False
    except NoCredentialsError:
        print("❌ AWS credentials not available")
        return False

upload_to_aws(FILE_PATH, BUCKET_NAME, S3_KEY)
