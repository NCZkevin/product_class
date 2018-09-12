"""ScProduct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from goods.views import GoodsViewSet, GoodsClassViewSet, GoodsKeywordViewSet


router = DefaultRouter()

#配置URL
router.register(r'goods', GoodsViewSet, base_name="goods")
router.register(r'key', GoodsKeywordViewSet, base_name="key")
router.register(r'class', GoodsClassViewSet, base_name="class")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('docx/', include_docs_urls(title='产品分类')),
    url(r'^', include(router.urls))

]
