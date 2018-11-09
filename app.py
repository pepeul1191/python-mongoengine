#!/usr/bin/env python
# encoding: utf-8

from configs.database import connect
from mongoengine import Document, StringField

class Collaborator(Document):
  meta = {'collection': 'collaborators', 'strict': False}
  name = StringField(required=True)

#'consultantId', 'className', 'name', 'userId', 'countryId

print("El primero")
print("++++++++++")
print(Collaborator.objects[0].name)
print("Todos")
print("+++++")
for d in Collaborator.objects:
  print(d.name)
