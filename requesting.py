import requests
import json
r = requests.get('https://api.datamuse.com/words?rel_rhy=carey')

print(type(r.text))
print(type(r.text))
print(type(r.json()[0]))
print(type(json.dumps(r.json(), indent = 2)))
print(r.headers)