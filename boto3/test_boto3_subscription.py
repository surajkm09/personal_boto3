import  boto3

client = boto3.client('sns')
response = client.subscribe(
    TopicArn='arn:aws:sns:us-west-2:776163741065:test_requests',
    Protocol='http',
    Endpoint=''
)
print(response)