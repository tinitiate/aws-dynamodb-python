import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='sbadmin', region_name='us-east-2')
dynamodb = session.client('dynamodb', endpoint_url='http://localhost:8000')

def delete_product(product_id):

    response = dynamodb.delete_item(
        TableName='Products',
        Key={
            'ProductID': {'N': str(product_id)}
        }
    )
    
    print("Product deleted:", response)

# Example usage
delete_product(123)