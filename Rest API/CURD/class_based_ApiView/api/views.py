from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView


class StudentAPI(APIView):
    # For get request
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(instance=stu)
            return Response(data=serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(instance=stu, many=True)
        return Response(data=serializer.data)


    # For post request
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Data is created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    # For Put request
    def put(self, request, pk=None, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(instance=stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Data is Complete Updated'})
        return Response(serializer.errors)


    # For Patch request
    def patch(self, request, pk=None, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(instance=stu,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Data is Partial Updated'})
        return Response(serializer.errors)

    
    # For Delete request
    def delete(self, request, pk=None, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"message" : "Data is Deleted"})