import boto3
import botocore

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='sbadmin', region_name='us-east-2')
dynamodb = session.client('dynamodb', endpoint_url='http://localhost:8000')

def retry_with_backoff():

    retry_count = 0
    max_retries = 3

    while retry_count < max_retries:
        try:
            response = dynamodb.put_item(
                TableName='Products',
                Item={
                    'ProductID': {'N': '123'},
                    'ProductName': {'S': 'Laptop'}
                }
            )
            print("Item added:", response)
            break  # Success, exit loop
        except botocore.exceptions.ClientError as e:
            print("Error:", e)
            retry_count += 1
            delay = 2 ** retry_count  # Exponential backoff
            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)

# Example usage
retry_with_backoff()