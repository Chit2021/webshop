#Import the Hero model
#Import the REST Framework serializer
#Create a new class that links the Cart with its serializer

from rest_framework import serializers

from .models import Cart

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ('item_id','item_name', 'item_price')