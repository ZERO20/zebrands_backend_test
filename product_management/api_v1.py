# -*- coding: utf-8 -*-

from django.urls import path, include
import apps.products.urls_v1 as products_api_v1
import apps.users.urls_v1 as users_api_v1

urlpatterns = [
    path('products/api/v1/',
        include((products_api_v1, 'apps.products'), namespace='products_api_v1'), name='products_v1'),
    path('users/api/v1/',
        include((users_api_v1, 'apps.users'), namespace='users_api_v1'), name='users_v1'),
]
