import json
import boto3

client = boto3.client('lambda')

def lambda_handler(event, context):
	inputForInvoker = {'CustomerId': '123', 'Amount': 50 }

	response = client.invoke(
		FunctionName='YOUR LAMBDA ARN',
		InvocationType='RequestResponse', # Event
		Payload=json.dumps(inputForInvoker)
		)

	responseJson = json.load(response['Payload'])

	print('\n')
	print(responseJson)
	print('\n')