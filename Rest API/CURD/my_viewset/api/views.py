from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import serializers, status
from rest_framework import viewsets


class StudentViewset(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(instance=stu, many=True)
        return Response(data=serializer.data)
    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(instance=stu)
            return Response(data=serializer.data)
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':"Data is created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(instance=stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':"Data is Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def partial_update(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(instance=stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':"Data is Partial Updated"})
        return Response(serializer.errors)
    def destroy(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'message':"Data is Deleted"})
