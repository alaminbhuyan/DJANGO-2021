from .models import Student
from .serializers import StudentSerializer
from rest_framework import serializers, status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from api.throttling import JackRateThrottle

class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # if use this class you have to configure 'rate' in setting.py file. Go and check
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]

    throttle_classes = [AnonRateThrottle, JackRateThrottle]