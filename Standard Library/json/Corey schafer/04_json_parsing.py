import json
from urllib.request import urlopen

with urlopen("https://api.github.com/users/hadley/orgs") as response:
    source = response.read()

# print(type(source)) # This is in bytes type
data = json.loads(source)
# print(type(data)) # This is list type
# print(json.dumps(data, indent=2))
with open('fetched_api_dat.json', 'w') as api:
    json.dump(data, api, indent=2)

for i in data:
    print(i['login'])
