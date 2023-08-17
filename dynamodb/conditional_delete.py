import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='sbadmin', region_name='us-east-2')
dynamodb = session.client('dynamodb', endpoint_url='http://localhost:8000')

def conditional_delete_product(product_id, max_price):

    response = dynamodb.delete_item(
        TableName='Products',
        Key={
            'ProductID': {'N': str(product_id)}
        },
        ConditionExpression='Price <= :max_price',
        ExpressionAttributeValues={
            ':max_price': {'N': str(max_price)}
        }
    )

    if response.get('Attributes'):
        print("Product deleted:", response)
    else:
        print("Product not deleted due to condition not met.")

# Example usage
conditional_delete_product(123, 1000.00)