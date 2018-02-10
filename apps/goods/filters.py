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
from django.db.models import Q


class GoodsFilter(django_filters.rest_framework.FilterSet):
    pricemin = django_filters.NumberFilter(name='shop_price', lookup_expr='gte')
    pricemax = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')
    top_category = django_filters.NumberFilter(method='')

    # Goods.objects.filter(shop_price__exact=)

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category_parent_category_id=value) | Q(
            category_parent_category_parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax']
