import json

# If we hace a Json string, we can parse it by using the json.loads()
data = '{"name":"Subhadeep Banerjee", "age": 30, "city": "Kolkata"}'
print(data)
print(type(data))
new_data = json.loads(data)
print(new_data)
print(type(new_data))

# So loads takes str and parse then into dict
