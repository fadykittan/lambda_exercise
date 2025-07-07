import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from sklearn.linear_model import LogisticRegression
import sklearn
import boto3
import os

bucket = os.environ.get('bucket')
print(bucket)
model = os.environ.get('model')
print(model)
vectiruzer = os.environ.get('vectiruzer')
print(vectiruzer)


s3 = boto3.client('s3')

# load midel pkl
response = s3.get_object(Bucket=bucket, Key=model)
body = response['Body'].read()
model = pickle.loads(body)

# load vectorizer pkl
response = s3.get_object(Bucket=bucket, Key=vectiruzer)
body = response['Body'].read()
vectorizer = pickle.loads(body)  

def is_spam(inp):
    print(inp)
    inp = pd.Series(inp)
    inp_test = vectorizer.transform(inp)
    inp_sonuc = model.predict(inp_test)

    if inp_sonuc == 'spam':
        return True
    else:
        return False

def lambda_handler(event, context):

    s3 = boto3.client('s3')

    s3_data = event['Records'][0]['s3'] 
    bucket = s3_data['bucket']['name']
    key = s3_data['object']['key']

    response = s3.get_object(Bucket=bucket, Key=key)
    data = response['Body'].read()

    sonuc = is_spam(data)
    print("sonuc", sonuc)

    # TODO implement
    return {
        'statusCode': 200  # ,
        # 'body': json.dumps({'result': sonuc})
    }
