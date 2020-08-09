import json
import requests

data = requests.get("https://status.aws.amazon.com/data.json")
# print (type(data))
d = data.json()
# print(d)
output = {}
l=[]
k = [values for key, values in d.items()]
for a in k:
    for items in a:  # item is a dict
        # print(items)
        for key, values in items.items():
            if "Region" in items[values]:
			    if key == "service":l.append(values)

#print(l)
output={a[0:3]:[a[4:]] for a in l if a =='ec2-us-east-1'}
print(output)


"""
if key in k.iteritems():
    for k, v in k.iteritems():
        print(k[j])
"""