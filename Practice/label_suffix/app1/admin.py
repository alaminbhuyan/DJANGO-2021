from django.contrib import admin
from .models import Mobile, Computer, UserProfile, UserProfile2

# Register your models here.
@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'brandName', 'modelName', 'price']


@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ['id', 'processor', 'motherboard', 'powerSupply', 'caseing', 'ram', 'total_price']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id','photo','user']


@admin.register(UserProfile2)
class UserProfileAdmin2(admin.ModelAdmin):
    list_display = ['id','photo']