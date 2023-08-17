# **DynamoDB**

## **Introduction to Amazon DynamoDB**

* Amazon DynamoDB is a fully managed NoSQL database service provided by Amazon Web Services (AWS). 
* It's designed for applications that require low-latency, scalable, and highly available storage solutions. 
* DynamoDB offers seamless scalability, automatic data replication, and built-in security features. 
* It's particularly suited for use cases where quick read and write operations are crucial, such as real-time applications, gaming leaderboards, and e-commerce platforms.

* DynamoDB uses a schema-less data model, where data is organized into tables consisting of items with attributes.

* Each item can have multiple attributes of varying types. 

* DynamoDB provides various features like flexible indexing, auto-scaling, and global replication for cross-region availability.

### **Data Types in Amazon DynamoDB**

* Amazon DynamoDB supports several data types for attributes within items. These data types are used to specify the format and structure of the data you store in your DynamoDB tables:

  - **String (S)**: Represents textual data. Examples include names, descriptions, and labels.

  - **Number (N)**: Represents numeric data, including integers and floating-point numbers.

  - **Binary (B)**: Stores binary data, such as images, audio, or video.

  - **Boolean (BOOL)**: Represents true or false values.

  - **String Set (SS)**: Represents a set of strings. Can be used for storing multiple distinct values.

  - **Number Set (NS)**: Represents a set of numbers.

  - **Binary Set (BS)**: Represents a set of binary data.

  - **List (L)**: Represents an ordered collection of values, including different data types. Lists can be nested.

  - **Map (M)**: Represents an unordered collection of key-value pairs, where the keys are strings and the values can be of different data types. Maps can be nested.

  - **Null (NULL)**: Represents a null value.

### **Data Modeling Concepts**

- **Primary Key**: Each item in a DynamoDB table requires a primary key, which can be either a simple primary key (partition key) or a composite primary key (partition key and sort key). The primary key uniquely identifies items within a table.
- **Partition Key**: A single attribute used to distribute data across partitions for scalability. It should be chosen based on your access patterns.
- **Sort Key**: If used in a composite primary key, it determines the order of items within a partition. It's helpful for range-based queries.
- **Secondary Indexes**: These allow you to query the table using attributes other than the primary key. Local Secondary Indexes (LSIs) are limited to the same partition key but can have different sort keys. Global Secondary Indexes (GSIs) can have different partition and sort keys.
- **Query**: A request to retrieve items from a table based on their primary key or indexed attributes.
- **Scan**: A request to retrieve all items in a table, filtering them based on specified conditions.
- **Projection**: The set of attributes included in the query or scan result. This can be a subset of the table's attributes.
- **Data Denormalization**: In DynamoDB, it's often beneficial to duplicate data across multiple items to optimize query performance. This is a trade-off between data storage and query speed.
- **Access Patterns**: Designing your data model to match the specific queries you need to perform. This involves choosing the right keys, indexes, and attributes.
- **Consistency**: DynamoDB offers eventual consistency and strongly consistent reads. Eventual consistency allows for faster reads, while strongly consistent reads provide up-to-date data.

### Terminology 

* **AttributeName:**
  - An attribute name refers to the name of an attribute that you define for your items in a table.
  - Each item in a DynamoDB table can have multiple attributes, which are essentially the pieces of data that you store for that item. 
  - The attribute name is used to uniquely identify each attribute within an item. 
* **KeyType:**
  - Key type indicates whether an attribute is used as the primary key and its role within the key structure.
  - DynamoDB uses two types of keys in its tables: 
    - Primary key and secondary index keys. 
    - The primary key consists of one or two attributes: the partition key (mandatory) and an optional sort key. 
    - The `KeyType` specifies whether an attribute is used as the partition key (`HASH`) or the sort key (`RANGE`) in the primary key or secondary index. 
* **ReadCapacityUnits:**
  - Read Capacity Units represent the number of read operations per second that a DynamoDB table can handle.
  - In DynamoDB, we provision read and write capacity units to manage the performance of your tables. 
  - Each read capacity unit can handle one strongly consistent read request per second or two eventually consistent read requests per second, where each request can read up to 4 KB of data. 
* **WriteCapacityUnits:**
  - Write Capacity Units represent the number of write operations per second that a DynamoDB table can handle.
  - Write capacity units are used to control the rate of write operations (such as put, update, and delete) on your DynamoDB table. 
  - Each write capacity unit can handle one write request per second, where each request can write up to 1 KB of data. If we provision 100 write capacity units, your table can handle 100 write requests per second.
* **Provisioned Throughput and Auto Scaling**
  - Provisioned Throughput: When creating a DynamoDB table, you provision read and write capacity units to specify the maximum number of read and write operations per second the table can handle.
  - Auto Scaling: DynamoDB offers auto-scaling, where read and write capacity can automatically adjust based on the workload to accommodate spikes in traffic while maintaining cost efficiency.
* **Consistency Models**
  - Eventually Consistent Reads: Allows for slightly stale data but offers lower latency. Read operations may not reflect the latest write.
  - Strongly Consistent Reads: Guarantees the most recent write has been retrieved. Offers higher latency compared to eventually consistent reads.
* **Indexes**
  - Local Secondary Index (LSI): An index that has the same partition key as the table but a different sort key. It's limited to the same partition key value as the base table.
  - Global Secondary Index (GSI): An index with a different partition and sort key from the base table. It provides more flexibility for querying data.
* **Item Collections:**
  - In DynamoDB, items with the same partition key are stored together in a collection. A partition key and sort key together define a primary key, and items with the same partition key are part of the same partition.
* **Capacity Modes:**
  - On-Demand Capacity Mode: Pay-per-request pricing. No need to provision read and write capacity units; DynamoDB automatically handles scaling.
  - Provisioned Capacity Mode: Traditional model where you explicitly provision read and write capacity units.
* **Batch Operations:**
  - DynamoDB supports batch operations for performing multiple operations in a single request. These operations include batch writes and batch gets.
* **Scan vs. Query:**
  - Scans read all items in a table or index. This operation can be resource-intensive and is often slower than queries.
  - Queries retrieve items using primary or secondary keys, making them more efficient for specific use cases.
* **Conditional Writes:**
  - DynamoDB allows you to write data conditionally based on the existence of an item or the values of its attributes.
* **Item Versioning and Conditional Updates:**
  - You can use conditional expressions to update items based on their current state, ensuring updates only occur when specific conditions are met.
* **Error Handling and Retries:**
  - DynamoDB operations can result in errors due to various reasons, such as exceeding provisioned capacity. Implement proper error handling and retries in your application.
* **Access Control and Security:**
  - Manage access to your DynamoDB tables using AWS Identity and Access Management (IAM) roles and policies.
  - Implement encryption at rest using AWS Key Management Service (KMS).
* **Streams:**
  - DynamoDB Streams captures changes to data in a table in real-time. You can use streams for various purposes, such as triggering Lambda functions or maintaining change logs.

## **Creating a Table**

```python
import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='your-profile-name', region_name='us-east-2')
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
```

## **Deleting a Table**

```python
import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='your-profile-name', region_name='us-east-2')
dynamodb = session.client('dynamodb', endpoint_url='http://localhost:8000')

def delete_table():
    response = dynamodb.delete_table(
        TableName='Products'
    )
    
    print("Table deleted:", response)

# Example usage
delete_table()

```

## **Create a New Product**

```python
import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='your-profile-name', region_name='us-east-2')
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

```

## Conditional Writes

```python
import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='your-profile-name', region_name='us-east-2')
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
```



## **Read Product Details**

```python
import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='your-profile-name', region_name='us-east-2')
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
```

## **Read all the Product Details**

```Python
import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='your-profile-name', region_name='us-east-2')
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
```

## **Update Product Stock**

```python
import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='your-profile-name', region_name='us-east-2')
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
```

##  **Item Versioning and Conditional Updates**

```python
import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='your-profile-name', region_name='us-east-2')
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
```

## **Delete a Product**

```python
import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='your-profile-name', region_name='us-east-2')
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
```

## Conditional Delete

```python
import boto3

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='your-profile-name', region_name='us-east-2')
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
```

## **Error Handling and Retries**

```python
import boto3
import botocore

# dynamodb = boto3.client('dynamodb')
# Configure Boto3 with your AWS profile and region
session = boto3.Session(profile_name='your-profile-name', region_name='us-east-2')
dynamodb = session.client('dynamodb', endpoint_url='http://localhost:8000')

def retry_with_backoff():

    retry_count = 0
    max_retries = 3

    while retry_count < max_retries:
        try:
            response = dynamodb.put_item(
                TableName='Products',
                Item={
                    'ProductID': {'N': '123'},
                    'ProductName': {'S': 'Laptop'}
                }
            )
            print("Item added:", response)
            break  # Success, exit loop
        except botocore.exceptions.ClientError as e:
            print("Error:", e)
            retry_count += 1
            delay = 2 ** retry_count  # Exponential backoff
            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)

# Example usage
retry_with_backoff()
```

