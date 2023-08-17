import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='sbadmin', region_name='us-east-2')
dynamodb = session.client('dynamodb', endpoint_url='http://localhost:8000')


def read_all_products():

    response = dynamodb.scan(
        TableName='Products'
    )

    products = response.get('Items', [])
    for product in products:
        print("Product:", product)

# Example usage
read_all_products()