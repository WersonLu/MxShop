#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     views_base
   Author :       aaa
   date：          2018/2/6
-------------------------------------------------
"""
from goods.models import Goods

from django.views.generic.base import View


class GoodsListView(View):
    def get(self, request):
        json_list = []
        goods = Goods.objects.all()[:10]
        # 比较初级的序列化,字段多容易出错,方法一
        # for good in goods:
        #     json_dict = {}
        #     json_dict["name"] = good.name
        #     json_dict["category"] = good.category.name
        #     json_dict["market_price"] = good.market_price
        #     # json_dict["add_time"] = good.add_time
        #     json_list.append(json_dict)
        # 方法二
        # from django.forms.models import model_to_dict
        # for good in goods:
        #     # 提取所有的字段
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        # 方法三 serializers 把所有字段序列化
        import json
        from django.core import serializers
        json_data = serializers.serialize("json", goods)
        json_data = json.loads(json_data)
        from django.http import HttpResponse, JsonResponse

        # 把存入列表字典数据,加载成json数据渲染到页面
        # 方法一二
        # return HttpResponse(json.dumps(json_list), content_type="application/json")
        # 方法三
        return JsonResponse(json_data, safe=False)
