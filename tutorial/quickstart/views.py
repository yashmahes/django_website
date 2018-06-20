from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from models import User, Shop, Product

from serializers import UserSerializer, ProductSerializer, ShopSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class ShopViewSet(viewsets.ModelViewSet):
	queryset = Shop.objects.all()
	serializer_class = ShopSerializer

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
