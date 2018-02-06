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
        # 比较初级的序列化
        for good in goods:
            json_dict = {}
            json_dict["name"] = good.name
            json_dict["category"] = good.category.name
            json_dict["market_price"] = good.market_price
            # json_dict["add_time"] = good.add_time
            json_list.append(json_dict)

        from django.http import HttpResponse
        import json
        return HttpResponse(json.dumps(json_list), content_type="application/json")
