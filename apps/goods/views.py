from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Goods, GoodsClass, GoodsKeyword, GoodsCategory
from .serializers import GoodsClassSerializer, GoodsKeywordSerializer, GoodsSerializer, CategorySerializer
# Create your views here.

class GoodsViewSet(viewsets.ModelViewSet):
    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()

class GoodsClassViewSet(viewsets.ModelViewSet):
    serializer_class = GoodsClassSerializer
    queryset = GoodsClass.objects.all()

class GoodsKeywordViewSet(viewsets.ModelViewSet):
    serializer_class = GoodsKeywordSerializer
    queryset = GoodsKeyword.objects.all()

class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
