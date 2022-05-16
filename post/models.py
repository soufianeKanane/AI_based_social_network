from django.db import models

from neomodel import   StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo, BooleanProperty


# Create your models here.


class Post(StructuredNode):
    id = UniqueIdProperty()
    body = StringProperty(unique_index=True)
    caption = StringProperty(unique_index=True)
    categories = StringProperty(unique_index=True)
    type = StringProperty(unique_index=True)
    isHidden = BooleanProperty(default=False)
    isPopolar = BooleanProperty(default=False)

    # Relations :
"""    city = RelationshipTo(City, 'LIVES_IN')
    friends = RelationshipTo('Person','FRIEND')"""


