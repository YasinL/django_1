#!/usr/bin/env python
# -*- conding:utf-8 -*-
from django.conf.urls import url
import django_app.views as views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
    # 用户管理URL
    url(r'^users/$', views.user_list, name='user_list'),
    url(r'^users/create/$', views.user_create, name='user_create'),
    url(r'^users/(?P<user_id>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^users/(?P<user_id>[0-9]+)/update/$', views.user_update, name='user_update'),
    url(r'^users/(?P<user_id>[0-9]+)/delete/$', views.user_delete, name='user_delete'),
    
    # 菜单管理URL
    url(r'^menus/$', views.menu_list, name='menu_list'),
    url(r'^menus/create/$', views.menu_create, name='menu_create'),
    url(r'^menus/(?P<menu_id>[0-9]+)/$', views.menu_detail, name='menu_detail'),
    url(r'^menus/(?P<menu_id>[0-9]+)/update/$', views.menu_update, name='menu_update'),
    url(r'^menus/(?P<menu_id>[0-9]+)/delete/$', views.menu_delete, name='menu_delete'),
]