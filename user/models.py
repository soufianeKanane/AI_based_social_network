from django.db import models
from neomodel import   StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo, BooleanProperty


# Create your models here.


class User(StructuredNode):
    id = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)
    email = StringProperty(index=True)
    password = StringProperty(index=True)


