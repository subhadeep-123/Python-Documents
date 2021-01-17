import json

# If we have a python object, we can convert it inyo a JSON string by using the, json.dumps() method.
data = {
    "Name": "Subhadeep Banerjee",
    "Age": 30,
    "City": "Kolkata"}
print(data)
print(type(data))
new_data = json.dumps(data, sort_keys=True)
print(new_data)
print(type(new_data))

# Okay to this convet a dict to JSON string
"""
dict
list
tuple
string
int
float
True
False
None
"""
# We can convert Python objects of the following types, into JSON strings.
