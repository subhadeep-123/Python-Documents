import json
from pprint import pprint
people_string = '''
{
    "people": [
        {
            "name": "Subhadeep Banerjee",
            "phone": "615-555-7164",
            "emails": ["abc123@gmail.com", "xyz999@hotmail.com"],
            "has_license": false
        },
        {
            "name": "Iam Matrix",
            "phone": "615-555-7164",
            "emails": null,
            "has_license": true
        }
    ]
}
'''
# print(people_string)
data = json.loads(people_string)
# print(data)
for people in data['people']:
    print(people['name'])
