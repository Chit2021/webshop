from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import CartSerializer
from .models import Cart


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by('item_id')
    serializer_class = CartSerializer
