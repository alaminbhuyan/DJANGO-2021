from django.contrib import admin
from .models import Post, Atricals

# Register your models here.
@admin.register(Post, Atricals)
class DefaultAdmin(admin.ModelAdmin):
    pass