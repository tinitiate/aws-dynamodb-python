# aws-dynamodb-python
## DynamoDB Python Scripts
- This repository contains a collection of Python scripts for interacting with AWS DynamoDB.
- These scripts provide examples of various operations such as creating tables, inserting data, querying, and deleting items in DynamoDB.

## Prerequisites
- Before you begin, make sure you have the following set up:

  - Python 3.x installed on your system.
  - AWS CLI configured with necessary credentials and region.
  - Docker with DynamoDB Local image running:
  - Install Docker on your machine if not already installed.
  - Run DynamoDB Local in a Docker container using the following command:
    ```bash
    docker run -p 8000:8000 amazon/dynamodb-local
    ```
  - The scripts will connect to the local DynamoDB instance by default. If you want to connect to the AWS service, adjust the DynamoDB client configuration in the scripts.
## Installation
 - Clone this repository to your local machine:

    ```bash
    git clone https://github.com/tinitiate/aws-dynamodb-python.git
    ```
- Navigate to the repository's directory:

  ```bash
  cd aws-dynamodb-python
  ```

- Usage
  - Run the desired script from the repository using the following command:

  ```bash
  python script_name.py
  ```
  - Replace script_name.py with the name of the script you want to run.

  - Follow the prompts or edit the script to modify the operations as needed.

## Scripts Overview
- create_table.py: Creates a new DynamoDB table.
- insert_data.py: Inserts sample data into the DynamoDB table.
- query_data.py: Demonstrates querying data from the table.
- delete_item.py: Deletes a specific item from the table.
- delete_table.py: Deletes the DynamoDB table.
