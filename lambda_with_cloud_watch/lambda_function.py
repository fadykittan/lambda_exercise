import json
import boto3

def lambda_handler(event, context):
    
    print("Received event:", event) # Print the event directly to see its structure

    # Access values directly from the 'event' dictionary
    loan_time = event["loan_time"]
    loan_amount = event["amount"]
    loan_survival = event["survival"]

    print(f"Loan Time: {loan_time}")
    print(f"Amount: {loan_amount}")
    print(f"Survival: {loan_survival}")

    results = {}

    results['c1'] = loan_time > 1
    if loan_time > 0:
        results['c2'] = (loan_amount / loan_time) <= 100000
    else:
        results['c2'] = False

    results['c3'] = loan_survival > 80

    final_result = results['c1'] and results['c2'] and results['c3']

    cloudwatch = boto3.client('cloudwatch')
    namespace = 'fady_bank_loan_metric' # Define your custom CloudWatch namespace

    metric_data = [
        {
            'MetricName': 'LoanTime',
            'Value': loan_time,
            'Unit': 'Count' # Or 'Seconds', 'None' depending on precise meaning
        },
        {
            'MetricName': 'LoanAmount',
            'Value': loan_amount,
            'Unit': 'None' # Or 'Currency', 'Dollars' if applicable
        },
        {
            'MetricName': 'LoanSurvival',
            'Value': loan_survival,
            'Unit': 'Percent' # Assuming survival is a percentage score
        },
        {
            'MetricName': 'Condition1Result',
            # Convert string 'True'/'False' to 1/0 for numerical metrics
            'Value': 1 if results['c1'] == 'True' else 0,
            'Unit': 'Count'
        },
        {
            'MetricName': 'Condition2Result',
            'Value': 1 if results['c2'] == 'True' else 0,
            'Unit': 'Count'
        },
        {
            'MetricName': 'Condition3Result',
            'Value': 1 if results['c3'] == 'True' else 0,
            'Unit': 'Count'
        }
    ]

    cloudwatch.put_metric_data(
        Namespace=namespace,
        MetricData=metric_data
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Final Result:' + str(final_result))
    }
