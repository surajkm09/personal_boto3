import boto3
def find_arn(topic):
    client = boto3.client('sns')
    response = client.list_topics()
    a = response['Topics']
    b=""
    ret=[]
    for j in topic:
        found=0
        for i in range(len(a)):

            b=a[i]
            b=str(b)
            b=b.split(':')[6]
            b=b[:len(b)-2]
            if b == j :
                temp=a[i]
                temp=str(temp)
                temp=temp[14:len(temp)-2]
                ret.append(temp)
                found=1
        if found==0:
            temp='invalid topic name'
            ret.append(temp)
    return ret
