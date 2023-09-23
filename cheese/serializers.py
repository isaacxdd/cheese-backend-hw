from .models import Cheese
from rest_framework import serializers


## Class CheeseSerializer is a subclass of serializers.HyperlinkedModelSerializer.
## For serializing and deserializing data into representations such as json.
class CheeseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cheese
        fields = ('id', 'name', 'origin_country', 'type')
