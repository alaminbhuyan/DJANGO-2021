import imp
from django.contrib import admin
from .models import UserSignUp


# Register your models here.
@admin.register(UserSignUp)
class UserSignUpModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password1']