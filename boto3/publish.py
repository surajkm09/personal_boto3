import boto3
import json

def publish(msg ,arn ):
    client = boto3.client('sns')

    response = client.publish(
        TopicArn=arn,
        Message=json.dumps({'default': json.dumps(msg)}),
        MessageStructure='json',

    )
    print(response)
if __name__ == '__main__':
    publish(msg,arn)