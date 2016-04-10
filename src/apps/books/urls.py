# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<id_book>[0-9]+)/$', views.book_detail, name='book_detail'),
    url(r'^(?P<id_book>[0-9]+)/(?P<id_page>[0-9]+)/$', views.page_detail, name='book_detail'),
]
