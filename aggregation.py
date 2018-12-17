#!/usr/bin/env python
# encoding: utf-8

from mongoengine import connect
from mongoengine import Document, StringField

connect('ubicaciones', host = '127.0.0.1', port = 27017)

class Location(Document):
  meta = {'collection': 'ubicaciones', 'strict': False}
  name = StringField(required=True, name='nombre')

for d in Location.objects:
  print(d.name)
