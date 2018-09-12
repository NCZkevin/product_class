from django.contrib import admin
from .models import Goods,GoodsClass,GoodsKeyword
# Register your models here.

admin.site.register([Goods, GoodsClass, GoodsKeyword])