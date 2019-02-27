
from Scrapping import *
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.unittest_pymongo

# method 1
dico_actor={}
for film in db.films.find():
    for actor in film.get('actors'):
        if actor not in dico_actor:
            dico_actor[actor.replace('\n','')]=[]
        dico_actor[actor.replace('\n','')].append(film.get('title').replace('\xa0',' '))
print(dico_actor)

print('######################################')
print('######################################')

# method 2
dico_actor2={}
for film in db.films.find():
  for actor in film['actors']:
    if actor not in dico_actor2:
      dico_actor2[actor.replace('\n','')]=[]
    dico_actor2[actor.replace('\n','')].append(film['title'])
print(dico_actor2)

client.close()

