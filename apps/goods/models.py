from django.db import models

# Create your models here.
# class GoodsClass(models.Model):  
#     name = models.CharField(max_length=100, verbose_name="类别名")

# class GoodsKeyword(models.Model):
#     name = models.CharField(max_length=100, verbose_name='关键字')
#     classes = models.ForeignKey(GoodsClass, blank=True, null=True, on_delete=models.SET_NULL)

class GoodsCategory(models.Model):
    """
    商品类别
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "关键词"),
    )

    name = models.CharField(max_length=100, verbose_name="类别名")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_cat", on_delete=models.SET_NULL) 

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Goods(models.Model):
    
    gtin = models.CharField(max_length=100, verbose_name="条码")
    company = models.CharField(max_length=100, verbose_name="公司名")
    spec = models.CharField(max_length=100, verbose_name="规格", blank=True)
    name = models.CharField(max_length=100, verbose_name="产品名")
    brand = models.CharField(max_length=100, verbose_name="品牌", blank=True, null=True)
    classes = models.ManyToManyField(GoodsCategory, blank=True, verbose_name="产品类目")
    is_class = models.IntegerField(default=0, verbose_name="是否分类")
    is_true = models.BooleanField(default=False, verbose_name="分类是否正确")

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

