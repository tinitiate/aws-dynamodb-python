import boto3
import random

# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='sbadmin', region_name='us-east-2')
dynamodb = session.client('dynamodb', endpoint_url='http://localhost:8000')

# List of real-world categories
categories = ['Electronics', 'Clothing', 'Books', 'Home and Kitchen', 'Beauty', 
              'Sports and Outdoors', 'Toys and Games', 'Health', 'Automotive', 'Jewelry']

# List of possible product name prefixes
product_name_prefixes = ['Premium', 'Deluxe', 'Eco-Friendly', 'Classic', 'Modern', 'Vintage', 'Innovative']

def generate_product_name():
    prefix = random.choice(product_name_prefixes)
    name = f'{prefix} Product'
    return name

def create_product(product_id, price, stock):
    product_name = generate_product_name()
    category = random.choice(categories)
    
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

# Insert 1000 records with real-world categories and generated product names
for i in range(1, 1000):
    create_product(i, i * 10.0, i * 5)
    
print("All records inserted.")
