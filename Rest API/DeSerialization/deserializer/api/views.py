from django.shortcuts import render
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

#! This decorator used for handle csrf verification when send post request
@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        # this is used to parse json data to python native data type
        python_data = JSONParser().parse(stream=stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response_data = {'message': "Data is created"}
            json_data = JSONRenderer().render(data=response_data)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(data=serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    return HttpResponse("hello world")
