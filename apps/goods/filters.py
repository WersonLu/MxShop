#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/2/7 16:45
 
'''
# 过滤查询器
import django_filters
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    price_min = django_filters.NumberFilter(name='shop_price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')

    # Goods.objects.filter(shop_price__exact=)

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']
