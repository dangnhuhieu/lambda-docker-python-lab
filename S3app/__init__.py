import os
from s3_function import upload_file_to_s3
from json_transform import transform_to_parquet

def ingest_to_s3():
    bucket_name = os.environ.get('BUCKET_NAME')
    file_name = os.environ.get('FILENAME')
    s3_job = upload_file_to_s3(file_name, bucket_name)
    print(s3_job)
    return s3_job

def lambda_ingest(event, context):
    s3_job = ingest_to_s3()
    if s3_job['status_code'] == '200':
        bucket_name = os.environ.get('BUCKET_NAME')
        tgt_folder = os.environ.get('TARGET_FOLDER')
        file_name = os.environ.get('FILENAME')
        transform_job = transform_to_parquet(file_name, bucket_name, tgt_folder)
        print(transform_job)
        return {
            'statusCode': 200,
            'statusMessage': 'File Transformed Successfully',
            'jobRunDetails': transform_job
        }
    else:
        return {
            'statusCode': 400,
            'statusMessage': 'Failed',
        }
