"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
import xadmin
from django.views.static import serve
from MxShop.settings import MEDIA_ROOT
# from goods.views_base import GoodsListView
from rest_framework.documentation import include_docs_urls
from goods.views import GoodsListViewSet, CategoryViewSet
from rest_framework.authtoken import views
# 视图路由配置
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()

router.register(r'goods', GoodsListViewSet, base_name="goods")
router.register(r'categorys', CategoryViewSet, base_name="categorys")
# goods_list = GoodsListViewSet.as_view({
#     'get': 'list',
# })
urlpatterns = [
    # 用第三方后台管理取代自带的
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # 商品列表页
    # url(r'^goods/$', goods_list, name="goods-list"),
    url(r'^', include(router.urls)),

    # url(r'^')
    url(r'^docs/', include_docs_urls(title="我的商城")),
    # drf 自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt 认证模式
    url(r'^login/', obtain_jwt_token),

]
