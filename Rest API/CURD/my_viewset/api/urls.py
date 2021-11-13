from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django import urls

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register(prefix='', viewset=views.StudentViewset, basename="student")

urlpatterns = [
    path('', include(router.urls))
]
