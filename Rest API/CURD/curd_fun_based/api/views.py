from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import io

# Create your views here.
@csrf_exempt
def studentAPI(request):
    # For Read data
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None) # grave the id from dict
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu) # create complex object
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        
        # For all object
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    # For Create data
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response_data = {'message' : "Data is created"}
            # json_data = JSONRenderer().render(data=response_data)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(response_data, safe=False) # when pass all data then self must be False

        json_data = JSONRenderer().render(data=serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    #  For Update data
    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        # Complete update --> Required all data from front end or client
        # serializer = StudentSerializer(instance=stu, data=python_data) should be like this
        # Partial Update --> all data not required
        serializer = StudentSerializer(instance=stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data = {'message' : "Data is Updated"}
            # json_data = JSONRenderer().render(data=response_data)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(response_data, safe=False)

        json_data = JSONRenderer().render(data=serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    # For Delete data
    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream=stream)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        response_data = {"message" : "Data is Deleted"}
        json_data = JSONRenderer().render(data=response_data)
        return HttpResponse(json_data, content_type='application/json')
    
    return HttpResponse("hello world")