from django.contrib import admin
from .models import EveryUserProfile


# Register your models here.

@admin.register(EveryUserProfile)
class EveryUserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'token', 'verify']