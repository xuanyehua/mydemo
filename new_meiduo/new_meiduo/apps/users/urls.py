from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^sms_codes/(?P<mobile>1[3-9]\d{9})/$', views.Sms.as_view()),

]