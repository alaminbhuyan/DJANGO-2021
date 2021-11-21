from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django import urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView



# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register(prefix='', viewset=views.StudentModelViewset, basename="student")

urlpatterns = [
    path('', include(router.urls)),
    path(route='gettoken/', view=TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(route='refreshtoken/', view=TokenRefreshView.as_view(), name="token_refresh"),
    path(route='verifytoken/', view=TokenVerifyView.as_view(), name="token_verify"),
]
