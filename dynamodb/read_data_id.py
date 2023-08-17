import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='sbadmin', region_name='us-east-2')
dynamodb = session.client('dynamodb', endpoint_url='http://localhost:8000')

def read_product(product_id):

    response = dynamodb.get_item(
        TableName='Products',
        Key={
            'ProductID': {'N': str(product_id)}
        }
    )
    
    product = response.get('Item')
    if product:
        print("Product:", product)
    else:
        print("Product not found.")

# Example usage
read_product(123)