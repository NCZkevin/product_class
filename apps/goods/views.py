from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Goods, GoodsCategory
from .serializers import GoodsSerializer, CategorySerializer, CompanySerializer, CategorySerializer3
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
    # queryset = Goods.objects.all()
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('gtin', 'name', 'is_class','brand','company')

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Goods.objects.all().order_by('id')
        isclass = self.request.query_params.get('is_class', None)
        isclick = self.request.query_params.get('is_click', None)
        if isclass is not None and isclick is not None:
            queryset = queryset.filter(is_class=isclass,is_click=isclick).order_by('id')
        elif isclick is None and isclass is not None:
            queryset = queryset.filter(is_class=isclass).order_by('id')
        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
    # pagination_class = CategoryPagination

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.values('company').distinct('company')
    serializer_class = CompanySerializer

class ClassesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.filter(category_type=2)
    serializer_class = CategorySerializer3