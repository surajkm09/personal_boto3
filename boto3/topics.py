import boto3

client = boto3.client('sns')
response = client.list_topics()
a=response['Topics']

print(len(a))

