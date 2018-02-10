#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/2/11 0:34
 
'''
import re
from datetime import datetime
from datetime import timedelta
from rest_framework import serializers
from .models import VerifyCode
from django.contrib.auth import get_user_model
from MxShop.settings import REGEX_MOBILE

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        # 验证手机
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已存在")
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号非法")

        on_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=60)
        if VerifyCode.objects.filter(add_time__gt=on_mintes_ago, mobile=mobile).count():
            raise serializers.ValidationError("未超过60秒")
