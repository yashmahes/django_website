from django.contrib import admin

# Register your models here.
from models import User, Shop, Product

admin.site.register(User)

admin.site.register(Shop)
admin.site.register(Product)
