import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='sbadmin', region_name='us-east-2')
dynamodb = session.client('dynamodb', endpoint_url='http://localhost:8000')

def update_stock(product_id, new_stock):

    response = dynamodb.update_item(
        TableName='Products',
        Key={
            'ProductID': {'N': str(product_id)}
        },
        UpdateExpression='SET Stock = :stock',
        ExpressionAttributeValues={
            ':stock': {'N': str(new_stock)}
        }
    )
    
    print("Product stock updated:", response)

# Example usage
update_stock(123, 8)