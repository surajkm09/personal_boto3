import boto3
from find_arn import find_arn
def find_subscribe (old_topics,new_topics,http_endpoint):
    topic_to_subscribe=list(set(new_topics) - set(old_topics))
    client = boto3.client('sns')
    print(topic_to_subscribe)
    topic_arn_to_subscribe=find_arn(topic_to_subscribe)
    if len(topic_arn_to_subscribe)!= 0 :
        for i in topic_arn_to_subscribe:
            client.subscribe(TopicArn=i,Protocol='http',Endpoint=http_endpoint)
    else:
        print("no topics to subscribe")
    topic_to_unsubscribe=list(set(old_topics) - set(new_topics))
    print(topic_to_unsubscribe)
    topic_arn_to_unsubscribe=find_arn(topic_to_unsubscribe)
    if len(topic_arn_to_unsubscribe)!=0:
        for i in topic_arn_to_unsubscribe:
            response=client.list_subscriptions_by_topic(TopicArn=i)
            subscribe_list=response['Subscriptions']
            for j in subscribe_list:
                if j['Endpoint']==http_endpoint:
                    client.unsubscribe(SubscriptionArn=j['SubscriptionArn'])
                    break
    else :
        print("no topics to unsubscribe")


