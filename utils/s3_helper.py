import boto3
import csv
import io
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def read_csv_from_s3(bucket: str, key: str):
    """Reads CSV from S3 and returns (rows:list[dict], headers:list[str]).
    Raises FileNotFoundError if object does not exist.
    """
    try:
        resp = s3.get_object(Bucket=bucket, Key=key)
    except ClientError as e:
        code = e.response.get('Error', {}).get('Code')
        if code in ("NoSuchKey", "404", "NoSuchBucket"):
            raise FileNotFoundError(f"{key} not found in bucket {bucket}")
        raise

    body = resp['Body'].read().decode('utf-8')
    f = io.StringIO(body)
    reader = csv.DictReader(f)
    rows = [r for r in reader]
    headers = reader.fieldnames if reader.fieldnames is not None else []
    return rows, headers


def write_csv_to_s3(bucket: str, key: str, rows: list, headers: list):
    """Writes rows (list of dict) to CSV and uploads to S3 (overwrites existing object).
    headers defines column order.
    """
    f = io.StringIO()
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    for r in rows:
        # ensure all headers present
        row = {h: r.get(h, "") for h in headers}
        writer.writerow(row)
    f.seek(0)
    s3.put_object(Bucket=bucket, Key=key, Body=f.getvalue().encode('utf-8'), ContentType='text/csv')
