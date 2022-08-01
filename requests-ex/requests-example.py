import requests

headers = {'Content_Type': 'application/json'}

r = requests.post('website', headers=headers)
print(r.text)
