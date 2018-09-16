# -*- coding: utf-8 -*-
import sys
import os
import pandas as pd

lld = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(lld)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ScProduct.settings')

import django
django.setup()

from goods.models import Goods, GoodsCategory

data = pd.read_csv('data/water_classnum.csv')
# from db_tools.data.product_data import row_data
for index,row in data.iterrows():
    # if index > 5:
    #     break
    # print(len(eval(row['classes'])))
    goods = Goods()
    goods.gtin = row['id']
    goods.company = row['company']
    goods.spec = row['spec']
    goods.name = row['name']
    goods.brand = row['brand']
    
    if len(eval(row['classes'])) > 0:
        goods.is_class = 1
        goods.save()
        classes = eval(row['classes'])
        for class_name in classes:
            category = GoodsCategory.objects.filter(name=class_name)
            goods.classes.add(category[0])
    else:
        goods.save()
    
    print(index)
# for goods_detail in row_data:
#     goods = Goods()
#     goods.name = goods_detail["name"]
#     goods.market_price = float(int(goods_detail["market_price"].replace("￥", "").replace("元", "")))
#     goods.shop_price = float(int(goods_detail["sale_price"].replace("￥", "").replace("元", "")))
#     goods.goods_brief = goods_detail["desc"] if goods_detail["desc"] is not None else ""
#     goods.goods_desc = goods_detail["goods_desc"] if goods_detail["goods_desc"] is not None else ""
#     goods.goods_front_image = goods_detail["images"][0] if goods_detail["images"] else ""

#     category_name = goods_detail["categorys"][-1]
#     category = GoodsCategory.objects.filter(name=category_name)
#     if category:
#         goods.category = category[0]
#     goods.save()

#     for goods_image in goods_detail["images"]:
#         goods_image_instance = GoodsImage()
#         goods_image_instance.image = goods_image
#         goods_image_instance.goods = goods
#         goods_image_instance.save()