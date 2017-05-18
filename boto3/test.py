import os
from find_arn import find_arn


def intial_arn_finder():
    dict_from_file={}
    with open('config.txt','r') as inf:
        dict_from_file = eval(inf.read())
    topics_arn_dict=dict_from_file['Topics']

    f=open('new_file','w')
    f.write('{\'Topics\':[')

    for i in range(len(topics_arn_dict)):
        topic=str(topics_arn_dict[i])
        topic=topic.split(':')
        topic=topic[0][2:len(topic[0])-1]
        #print(topic)
        arn=find_arn(topic)
        f.write('{\'%s\':\'%s\'},' % (topic, arn))

    f.write('],')
    b = dict_from_file['NextToken']
    f.write('\'NextToken\':')
    f.write('\'%s\'}'%b)
    os.remove('config.txt')
    os.rename('new_file','config.txt')
if __name__ == '__main__':
    intial_arn_finder()



