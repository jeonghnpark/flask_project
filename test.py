import requests
base_url = "http://hn.algolia.com/api/v1"
id="16582136"

def make_detail_url(id):
    return f"{base_url}/items/{id}"

url = make_detail_url(id)
d=requests.get(make_detail_url(id)).json()
# print(d['children'])
for c in d['children']:
    print(c['text'])