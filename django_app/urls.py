#!/usr/bin/env python
# -*- conding:utf-8 -*-
from django.conf.urls import  url
import  django_app.views as views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
    # url(r'^django_app/latest\.html',views.index)

]