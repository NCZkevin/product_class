# -*- coding: utf-8 -*-

#独立使用django的model
import sys
import os


pwd = os.path.dirname(os.path.realpath(__file__))
lld = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(lld)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ScProduct.settings')
import django
django.setup()

from goods.models import GoodsCategory

from db_tools.data.category_data import classify

lev1_intance = GoodsCategory()
lev1_intance.name = '饮料'
lev1_intance.category_type = 1
lev1_intance.save()
for class1 in classify:
    lev2_intance = GoodsCategory()
    lev2_intance.name = classify[class1][0]
    lev2_intance.category_type = 2
    lev2_intance.parent_category = lev1_intance
    lev2_intance.save()
    for keyword in classify[class1][1]:
        lev3_intance = GoodsCategory()
        lev3_intance.name = keyword
        lev3_intance.category_type = 3
        lev3_intance.parent_category = lev2_intance
        lev3_intance.save()