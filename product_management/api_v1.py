# -*- coding: utf-8 -*-

from django.urls import path, include


urlpatterns = [
    path('products/', include('apps.products.urls_v1')),
    path('users/', include('apps.users.urls_v1')),
]
