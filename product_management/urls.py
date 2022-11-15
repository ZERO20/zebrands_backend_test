"""product_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib import admin
from django.urls import include, path, re_path

import product_management.api_v1 as api_v1

schema_view = get_schema_view(
    openapi.Info(
        title="Product Management",
        default_version='v1',
        description="Product Management",
        contact=openapi.Contact(email="edgargdcv@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


class HealthCheckAPIView(APIView):
    """Health Check for the API"""

    def get(self, request):
        return Response(data={"status": "Hello world!"}, status=status.HTTP_200_OK)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HealthCheckAPIView.as_view(), name='health-check'),
    path('api/v1/', include((api_v1, 'product_management'), namespace='api_v1')),
    re_path(
        r'^docs/$', schema_view.with_ui('swagger',cache_timeout=0),
        name='schema-swagger-ui'
    ),
]
