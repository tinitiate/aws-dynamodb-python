import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='sbadmin', region_name='us-east-2')
dynamodb = session.client('dynamodb', endpoint_url='http://localhost:8000')

def create_product(product_id, product_name, price, stock, category):
    response = dynamodb.put_item(
        TableName='Products',
        Item={
            'ProductID': {'N': str(product_id)},
            'ProductName': {'S': product_name},
            'Price': {'N': str(price)},
            'Stock': {'N': str(stock)},
            'Category': {'S': category}
        }
    )
    
    print("Product created:", response)

# Example usage
create_product(123, 'Laptop', 999.99, 10, 'Electronics')