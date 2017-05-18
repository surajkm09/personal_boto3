import subprocess
if __name__ == '__main__':
    output=subprocess.call(['python3','http_mongo_endpoint.py','&'],stdout=subprocess.PIPE)
    print(output)

    output=subprocess.call(['python3', 'watch_dog.py','&'],stdout=subprocess.PIPE)
    print(output)
    print('ariba')