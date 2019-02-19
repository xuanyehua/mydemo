import random

from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from mydemo.new_meiduo.new_meiduo.apps.users.yuntongxun.sms import CCP
from .models import *

class Sms(APIView):
    def get(self,request,mobile):
        print(mobile)
        mobile_sql=User.objects.filter(mobile=mobile)
        print(mobile)
        print(type(mobile))
        if mobile_sql:
            return HttpResponse("号码已存在")
        redis = get_redis_connection("default")
        redis_mobile=redis.get(mobile)
        print(redis_mobile)
        if redis_mobile:
            return HttpResponse("发送短信过于平凡")
        sms_code = '%06d' % random.randint(0, 999999)
        pl = redis.set(mobile,1000,sms_code)
        ccp=CCP()
        ccp.send_template_sms(mobile,[sms_code,800],1)
        return HttpResponse({"message":"ok"})

