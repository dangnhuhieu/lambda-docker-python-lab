import boto3
import requests

def upload_file_to_s3(file_name, bucket_name):
    print(f'Getting the {file_name} from gharchive')
    res = requests.get(f'https://data.gharchive.org/{file_name}')
    print(f'Uploading {file_name} to s3 under s3://{bucket_name}')
    s3_client = boto3.client('s3', region_name="ap-northeast-1")
    upload_res = s3_client.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=res.content
    )

    objects = s3_client.list_objects(Bucket=bucket_name)['Contents']
    objectname= []
    for obj in objects:
        objectname.append(obj['Key'])

    return {
        'object_names': objectname,
        'status_code': '200'
    }