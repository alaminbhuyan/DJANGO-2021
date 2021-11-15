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
    path('', include(router.urls)),
    # When use SessionAuthentication use this path for login promot
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
