from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Goods, GoodsClass, GoodsKeyword
from .serializers import GoodsClassSerializer, GoodsKeywordSerializer, GoodsSerializer
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

