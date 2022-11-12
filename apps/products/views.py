
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckAPIView(APIView):
    """Health Check for the API"""

    def get(self, request):
        return Response(data={"status": "Hello world!"}, status=status.HTTP_200_OK)
