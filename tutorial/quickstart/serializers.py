

from rest_framework import serializers

from models import User, Shop, Product

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('firstname', 'lastname', 'profileimage', 'username', 'email', 'password', 'mobile')

class ShopSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Shop
		fields = ('category', 'location', 'area', 'UnitPrice', 'SellingPrice')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields = ('name', 'description', 'sku', 'variant', 'UnitPrice', 'SellingPrice')



