import json

with open('states.json') as f:
    data = json.load(f)

# print(type(data))
# print(data)
# data = json.dumps(data, indent=2)
# print(type(data))
# print(data)

with open('newstates.json', 'w') as f:
    json.dump(data, f, indent=2)
