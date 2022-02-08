from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# Create your views here.
# @api_view()
# def studentAPI(request):
#     return Response({"message" : "Hello world"})

# --------------------------------------------------------------------

# @api_view(['GET']) # GET have by default
# def studentAPI(request):
#     return Response({"message" : "Hello world"})

# @api_view(['POST'])
# def studentAPI(request):
#     if request.method == "POST":
#         return Response({"message" : "This is Post"})

# --------------------------------------------------------------------

# @api_view(['GET','POST'])
# def studentAPI(request):
#     if request.method == "GET":
#         return Response({"message" : "This is Get Request"})

#     if request.method == "POST":
#         return Response({"message" : "This is Post Request", 'data' : request.data})

# -------------------------------------------------------------------------------------------

# @api_view(['GET','POST', 'PUT', 'PATCH' 'DELETE'])
# def studentAPI(request):
#     if request.method == "GET":
#         id = request.data.get('id')
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(instance=stu)
#             return Response(data=serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(instance=stu, many=True)
#         return Response(data=serializer.data)

#     # For post request
#     if request.method == "POST":
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message' : 'Data is created'})
#         return Response(serializer.errors)

#     # For Put request
#     if request.method == "PUT":
#         id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(instance=stu,data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message' : 'Data is Updated'})
#         return Response(serializer.errors)

#     # For Delete request
#     if request.method == "DELETE":
#         id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({"message" : "Data is Deleted"})

# -------------------------------------------------------------------------------------------


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def StudentAPI(request, pk=None):
    if request.method == "GET":
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(instance=stu)
            return Response(data=serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(instance=stu, many=True)
        return Response(data=serializer.data)

    # For post request
    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data is created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # For Put request
    if request.method == "PUT":
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(instance=stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data is Complete Updated'})
        return Response(serializer.errors)

    # For Patch request
    if request.method == "PATCH":
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(
            instance=stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data is Partial Updated'})
        return Response(serializer.errors)

    # For Delete request
    if request.method == "DELETE":
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"message": "Data is Deleted"})
