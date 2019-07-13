from elasticsearch import Elasticsearch
from pprint import pprint
import datetime
import json
import requests, json, os
import sys

today    = datetime.date.today()
directory = 'news-please-repo/data/'
INDEX_NAME = 'news_'+str(today)
TYPE = "document" # ?? what's this?


es = Elasticsearch(hosts=[{"host":"127.0.0.1", "port":9200}])

print("Creating index: " + INDEX_NAME)
# create an index, ignore if it exists already
try:
	es.indices.delete(index=INDEX_NAME)
	es.indices.create(index=INDEX_NAME)
except Exception as e:
	print("ERROR: ES server unreachable.")
	pprint(e)
	exit(1)
i=0
print("Adding files")
for (root, subs, files) in os.walk('.'):
	for name in [file for file in files if file.endswith(".json")]:
		# print(root+"\\"+name)
		with open(root+'\\'+name, 'rb') as f:
			try:
				s = json.load(f)
				# pprint(s)
				print(INDEX_NAME, str(i), name)
				# add a single document
				out = es.create(id=i, index=INDEX_NAME, doc_type='document', body=s)
				# print(out)
			except Exception as e:
				# probably bad json
				# print(" on "+ name)
				# pprint(str(e.__dir__()))
				try:
					print('ERROR', e.status_code)
					pprint(e.info)
				except Exception as e2:
					print('ERROR', e.msg)
					# print(e2.error)
		i=i+1
				
count = es.count(index=INDEX_NAME, doc_type=TYPE, body={ "query": {"match_all" : { }}})
print(i)
# now we can do searches.
print("There are {0} documents.".format(count['count']))
while True:
    try:
        query = input("Enter a search: ")
        result = es.search(index=INDEX_NAME, body={"query": {"match": {"text": query.strip()}}})
        if result.get('hits') is not None and result['hits'].get('hits') is not None:
            print(result['hits']['hits'])
            print(len(result['hits']['hits']), " results.")
        else:
            print({})
    except(KeyboardInterrupt):
        break