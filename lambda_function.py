import json
from app import save_to_s3

def lambda_handler(event, context):
    
    # Parse the JSON body from the event
    try:
        data = json.dumps(event)
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid JSON format'})
        }
    
    # Call the save_to_s3 function from app.py
    result, status_code = save_to_s3(data)
    
    print(result)
    print(status_code)
    # Return the response in Lambda format
    return {
        'statusCode': status_code,
        'body': json.dumps(result)
    }

# for testing locally
if __name__ == '__main__':
    lambda_handler({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}, {})