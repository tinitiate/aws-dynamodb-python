import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='sbadmin', region_name='us-east-2')
dynamodb = session.client('dynamodb', endpoint_url='http://localhost:8000')

def conditional_update_price(product_id, new_price, expected_price):

    response = dynamodb.update_item(
        TableName='Products',
        Key={
            'ProductID': {'N': str(product_id)}
        },
        UpdateExpression='SET Price = :new_price',
        ConditionExpression='Price = :expected_price',
        ExpressionAttributeValues={
            ':new_price': {'N': str(new_price)},
            ':expected_price': {'N': str(expected_price)}
        }
    )
    
    if response.get('Attributes'):
        print("Price updated:", response)
    else:
        print("Price not updated due to condition not met.")

# Example usage
conditional_update_price(123, 899.99, 999.99)