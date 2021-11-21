from django.urls import path, include
from app1.api import views
from rest_framework.routers import DefaultRouter


# Create router object
router = DefaultRouter()
router.register(prefix='crud', viewset=views.UserViewSet, basename='user')

urlpatterns = [
    path(route='', view=include(router.urls))
]
