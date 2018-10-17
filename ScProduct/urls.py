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

from goods.views import GoodsViewSet, CategoryViewSet, CompanyViewSet, ClassesViewSet
from goods.views_index import DashboardView, RuleCompanyView, FileUploadView

router = DefaultRouter()

#配置URL
router.register(r'goods', GoodsViewSet, base_name="goods")
router.register(r'categorys', CategoryViewSet, base_name="categorys")
router.register(r'company', CompanyViewSet, base_name="company")
router.register(r'classes',ClassesViewSet, base_name="classes")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docx/', include_docs_urls(title='产品分类')),
    path('dashboard', DashboardView),
    path('rule/company/', RuleCompanyView),
    path('upload/', FileUploadView.as_view()),
    url(r'^', include(router.urls))

]
