import json
import uuid


def lambda_handler(event, context):
    #1 - Read off the input arguments
    CustomerId = event['CustomerId']

    #2 - Generate a random id
    transactionId = str(uuid.uuid1())

    #3 Do something i.e. save to s3, write to database, launch ec2 instance, etc ...

    #4 - Format and return response

    return {'CustomerId': custmoerId, 'Success': 'true', 'TransactionId': transactionId}
