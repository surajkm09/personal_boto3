with open('test_.txt', 'r') as inf:
    payload = eval(inf.read())
print(payload["Topics"][0])