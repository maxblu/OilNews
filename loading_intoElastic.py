#THis don't work
import requests, json, os
from elasticsearch import Elasticsearch


directory = 'news-please-repo/data/'

res = requests.get('http://localhost:9200')
print (res.content)
es = Elasticsearch()

i = 1

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        f = open(filename)
        print('Loading')
        docket_content = f.read()
        # Send the data into es
        es.index(index='news', doc_type='Articles', 
        id=i, body=json.loads(docket_content))
        i = i + 1