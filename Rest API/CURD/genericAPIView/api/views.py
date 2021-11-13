from django.views.generic import GenericViewError
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

# List and Create --> pk not required
class LCStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request=request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request=request, *args, **kwargs)

# Retrive, Update, Delete --> pk required
class RUDStudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request=request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request=request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request=request, *args, **kwargs)