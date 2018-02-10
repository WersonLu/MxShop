from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from django.db.models import Q
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from users.serizlizers import SmsSerializer
from rest_framework.response import Response
from rest_framework import status
from utils.yunpian import YunPian

User = get_user_model()
from MxShop.settings import APIKEY

class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SmsCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    """发送短信验证码"""
    # 验证手机号
    serializer_class = SmsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data["mobile"]
        yun_pian=YunPian

