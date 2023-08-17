import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='sbadmin', region_name='us-east-2')
dynamodb = session.client('dynamodb', endpoint_url='http://localhost:8000')

def conditional_update_stock(product_id, new_stock, min_stock):

    response = dynamodb.update_item(
        TableName='Products',
        Key={
            'ProductID': {'N': str(product_id)}
        },
        UpdateExpression='SET Stock = :new_stock',
        ConditionExpression='Stock > :min_stock',
        ExpressionAttributeValues={
            ':new_stock': {'N': str(new_stock)},
            ':min_stock': {'N': str(min_stock)}
        }
    )
    
    if response.get('Attributes'):
        print("Product stock updated:", response)
    else:
        print("Stock not updated due to condition not met.")

# Example usage
conditional_update_stock(123, 7, 5)