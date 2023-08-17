import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='sbadmin', region_name='us-east-2')
dynamodb = session.client('dynamodb', endpoint_url='http://localhost:8000')

# Create a new DynamoDB table
def create_table():
    response = dynamodb.create_table(
        TableName='Products',
        KeySchema=[
            {
                'AttributeName': 'ProductID',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'ProductID',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print("Table created:", response)
create_table()