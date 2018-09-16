from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Goods, GoodsCategory
from .serializers import GoodsSerializer, CategorySerializer
# Create your views here.

class GoodsPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class CategoryPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class GoodsViewSet(viewsets.ModelViewSet):
    """
    商品列表页, 分页， 搜索， 过滤， 排序
    """
    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('gtin', 'name', 'is_class','brand','company')

class CategoryViewset(viewsets.ModelViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
    # pagination_class = CategoryPagination
