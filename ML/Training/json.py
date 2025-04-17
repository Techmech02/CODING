import json
data=["apple","banana","guava"]
with open("data.json",'w') as f:
    json.dumps(data,f)
