#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/2/7 13:59
 
'''
from rest_framework import serializers

from goods.models import Goods, GoodsCategory


# 把需要的字段序列化为json 方法一
# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100, required=True)
#     click_num = serializers.IntegerField(default=0)
#     #
#     goods_front_image = serializers.ImageField(0)
#
#     # def create(self, validated_data):
#     #     return Goods.objects.create(**validated_data)
# 方法二

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory

        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model = Goods
        # fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = "__all__"
