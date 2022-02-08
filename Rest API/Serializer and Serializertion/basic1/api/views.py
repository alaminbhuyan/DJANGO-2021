from django.shortcuts import render, HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse


# Model object for single Student data


def home(request):
    student = Student.objects.get(id=1)
    serializer = StudentSerializer(instance=student)
    json_data = JSONRenderer().render(serializer.data)  # no need when use JsonResponse
    # no need when use JsonResponse
    return HttpResponse(json_data, content_type='application/json')

    # We can also use JsonResponse
    # return JsonResponse(serializer.data, safe=True) # By default safe=True


def studentInfo(request, pk):
    student = Student.objects.get(pk=pk)
    serializer = StudentSerializer(instance=student)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

# Model object for all Student data


def studentInfo2(request):
    student = Student.objects.all()
    serializer = StudentSerializer(instance=student, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

    # If we use JsonResponse for all objects then use safa=False
    # return JsonResponse(serializer.data, safe=False) # By default safe=True
