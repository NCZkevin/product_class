from django.views.generic.base import View
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import json
from goods.models import Goods, GoodsCategory
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
import pandas as pd

# def get_parameter_dic(request, *args, **kwargs):
#     # if isinstance(request, Request) == False:
#     #     return {}

#     query_params = request.query_params
#     if isinstance(query_params, QueryDict):
#         query_params = query_params.dict()
#     result_data = request.data
#     if isinstance(result_data, QueryDict):
#         result_data = result_data.dict()

#     if query_params != {}:
#         return query_params
#     else:
#         return result_data

@api_view(['GET', 'POST'])
def DashboardView(request):
    total = Goods.objects.all().count()
    is_class = Goods.objects.filter(is_class=1).count()
    no_class = total - is_class
    class_per = round(is_class / total,2)
    return Response({
        "total": total,
        "is_class": is_class,
        "no_class": no_class,
        "percent": class_per*100
    })

@api_view(['POST'])
def RuleCompanyView(request):
    params=request.data
    # print(params)
    goods = Goods.objects.filter(company=params['comy'])
    category = GoodsCategory.objects.filter(name=params['categ'])
    num = 0
    for good in goods:
        if good.is_class == 0:
            num += 1
            good.is_class = 1
            good.classes.add(category[0])
    return Response({
        "num": num,
        "message": "succeess"
    })

class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        file_obj = request.data["file"]
        data = pd.read_excel(file_obj)
        try:
            for index,row in data.iterrows():
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
        except Argument:
            print(Argument)
            return Response({
                "msg": "上传文件失败，请检查文件格式是否正确"
            })
        else:
            return Response(status=201,data = 
            {   "code": 201,
                "msg": "上传数据成功"
            })
        # print(data)
        # print("here")

        # return Response(status=201)

# def DashboardView(self):
#     total = Goods.objects.all().count()
#     is_class = Goods.objects.filter(is_class=1).count()
#     no_class = total - is_class
#     class_per = is_class / total
#     json_data = {
#         "total": total,
#         "is_class": is_class,
#         "no_class": no_class,
#         "percent": class_per
#     }
#     return JsonResponse(json_data,safe=False)
# class DashboardView(View):
#     def get(self, request):
#         total = Goods.objects.all().count()
#         is_class = Goods.objects.filter(is_class=1).count()
#         no_class = total - is_class
#         class_per = is_class / total
#         json_data = {
#             "total": total,
#             "is_class": is_class,
#             "no_class": no_class,
#             "percent": class_per
#         }
#         return JsonResponse(json.dump(json_data),safe=False)