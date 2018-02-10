from django.shortcuts import render

# Create your views here.

from goods.serializer import GoodsSerializer, CategorySerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response

from rest_framework import mixins, viewsets
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Goods, GoodsCategory
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter

from rest_framework import filters
from rest_framework.authentication import TokenAuthentication


# 商品分页设置
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = "page"


# 商品列表页接口
# 方法一
# class GoodsListView(APIView):
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)
# drf的request
# def post(self,request):
#     # 处理前段post提交的数据,并给出返回
#     serializer=GoodsSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# 方法二
# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
# queryset = Goods.objects.all()
# serializer_class = GoodsSerializer
#
# def get(self, request, *args, **kwargs):
#     return self.list(request, *args, **kwargs)

# 方法三
# class GoodsListView(generics.ListAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsPagination

# 方法四
class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页,分页,搜素,过滤,排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    # 分页
    pagination_class = GoodsPagination
    # token 验证
    authentication_classes = (TokenAuthentication,)
    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get("price_min", 0)
    #     if price_min:
    #         Goods.objects.filter(shop_price_gt=int(price_min))
    #     return queryset
    # 过滤器
    # filter_backends = (DjangoFilterBackend,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('name', 'shop_price')
    filter_class = GoodsFilter
    # 搜索也可设置条件,模糊,精确等
    search_fields = ('name', 'goods_desc')
    # 排序
    ordering_fields = ('sold_num', 'shop_price')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    商品分类数据
    """
    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer
