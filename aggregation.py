#!/usr/bin/env python
# encoding: utf-8

from mongoengine import connect
from mongoengine import Document, StringField
from bson.objectid import ObjectId
from bson.son import SON
from pymongo import MongoClient
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

search = 'La V'

pipeline = [
  {
    '$match': {
      'tipo': 'distrito'
    }
  },
  {
    '$lookup': {
      'from': 'ubicaciones',
      'localField': 'provincia_id',
      'foreignField': '_id',
      'as': 'provincia'
    }
  },
  {
    '$unwind': {
      'path': '$provincia',
      'preserveNullAndEmptyArrays': True
    }
  },
  {
    '$lookup': {
      'from': 'ubicaciones',
      'localField': 'provincia.departamento_id',
      'foreignField': '_id',
      'as': 'departamento'
    }
  },
  {
    '$unwind': {
      'path': '$departamento',
      'preserveNullAndEmptyArrays': True
    }
  },
  {
    '$match':{
      'departamento.pais_id': ObjectId('5b90a5b1ef627560f1251e4d'),
      'nombre': {
        '$regex': '^' + search
      }
    }
  },
  {
    '$project': {
      '_id': '$_id',
      'nombre': {
        '$concat': [
          '$nombre',
          ', ',
          '$provincia.nombre',
          ', ',
          '$departamento.nombre'
        ]
      },
    }
  },
  {
    '$limit': 10
  },
]


cursor = Location.objects.aggregate(*pipeline)

for d in list(cursor):
  print(d)

#pprint.pprint(list(cursor))
