import boto3
import json
import uuid
import os

# Configure your S3 bucket name and folder
S3_BUCKET = 'fady-my-bucket'  # <-- CHANGE THIS
S3_FOLDER = 'lambda_exe2/raw-data/'

# Initialize S3 client (assumes AWS credentials are set in environment or config)
s3_client = boto3.client('s3')

def save_to_s3(data):
    # if not data or not all(k in data for k in ('name', 'city', 'age')):
    #     return {}, 400

    # Generate a unique filename
    filename = f"{uuid.uuid4()}.json"
    s3_key = os.path.join(S3_FOLDER, filename)

    # Convert data to JSON string
    json_data = json.dumps(data)

    print('converted!')
    print(json_data)
    try:
        print(s3_key)
        s3_client.put_object(Bucket=S3_BUCKET, Key=s3_key, Body=json_data, ContentType='application/json')
        return json_data, 200
    except Exception as e:
        print(e)
        return {}, 500

if __name__ == '__main__':
    save_to_s3()