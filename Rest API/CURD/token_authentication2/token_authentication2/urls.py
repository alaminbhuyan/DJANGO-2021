
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='', view=include("api.urls")),
]

# Username: superuser, user1
# Password: superuser, geekyshows
