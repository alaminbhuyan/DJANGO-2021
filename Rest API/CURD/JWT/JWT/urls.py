from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='', view=include("api.urls")),
]

# username: superuser, user1,
# password: superuser, geekyshows