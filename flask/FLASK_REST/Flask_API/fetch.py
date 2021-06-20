import requests

# Requesting root
resp = requests.get('http://127.0.0.1:5000')
print(resp.json())


# Requesting /quarks
resp = requests.get('http://127.0.0.1:5000/quarks')
obj = resp.json()
print(obj)
print(obj['quarks'][0]['name'])
print(obj['quarks'][1]['charge'])

# Requesting only one item
resp = requests.get('http://127.0.0.1:5000/quarks/up')
print(resp.json())


# Requesting a Put req
resp = requests.post('http://127.0.0.1:5000/quarks',
                     json={"name": "top", "charge": "+2/3"})
print(resp.json())
