#!/usr/bin/env python
# encoding: utf-8

from mongoengine import connect
from mongoengine import Document, StringField
import pprint

connect('ubicaciones', host = '127.0.0.1', port = 27017)

class Location(Document):
  meta = {'collection': 'ubicaciones', 'strict': False}
  name = StringField(required=True, name='nombre')
  type = StringField(required=True, name='tipo')
  country_id = StringField(required=False, name='pais_id')
  department_id = StringField(required=False, name='departamento_id')
  province_id = StringField(required=False, name='provincia_id')

for d in Location.objects:
  pass
  #print(d.name)

pipeline = [
  {
    '$match': {
      'tipo': 'distrito'
    }
  },
]

cursor = Location.objects.aggregate(*pipeline)

print(list(cursor))

for d in list(cursor):
  print(d)

pprint.pprint(list(cursor))
