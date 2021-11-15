from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import serializers, status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

# Here I use ModelViewSet class 
# -----------------------------------------------------------------------------------------------------------------
                                            # This is for BasicAuthentication #
# -----------------------------------------------------------------------------------------------------------------
# class StudentViewset(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [BasicAuthentication]
#     # it gives access only authenticated user
#     # permission_classes = [IsAuthenticated] 

#     # it gives access all user
#     # permission_classes = [AllowAny] 

#     # it gives access when the staff-status will be True
#     permission_classes = [IsAdminUser]
    

    # Note if you want to apply globally this technique then go to settings.py file and see the below code


# -----------------------------------------------------------------------------------------------------------------
                                            # This is for SessionAuthentication #
# -----------------------------------------------------------------------------------------------------------------
class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]