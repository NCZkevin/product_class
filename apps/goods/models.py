from django.db import models

# Create your models here.
class GoodsClass(models.Model):  
    name = models.CharField(max_length=100, verbose_name="类别名")

class GoodsKeyword(models.Model):
    name = models.CharField(max_length=100, verbose_name='关键字')
    classes = models.ForeignKey(GoodsClass, blank=True, null=True, on_delete=models.SET_NULL)

class Goods(models.Model):
    
    gtin = models.IntegerField()
    company = models.CharField(max_length=100, verbose_name="公司名")
    spec = models.CharField(max_length=100, verbose_name="规格", blank=True)
    name = models.CharField(max_length=100, verbose_name="产品名")
    brand = models.CharField(max_length=100, verbose_name="品牌", blank=True, null=True)
    classes = models.ManyToManyField(GoodsClass, blank=True)
