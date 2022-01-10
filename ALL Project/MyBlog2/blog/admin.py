from django.contrib import admin
from .models import (PythonBlogPost, DjangoBlogPost, 
MLBlogPost, DLBlogPost, AboutUs, Contact)
from .forms import (PythonBlogAdminForm, DjangoBlogAdminForm,
 MLBlogAdminForm, DLBlogAdminForm, AboutUsAdminForm)


# Register your models here.

@admin.register(PythonBlogPost)
class PythonBlogPostAdmin(admin.ModelAdmin):
    form = PythonBlogAdminForm
    list_display = ['id','title']


@admin.register(DjangoBlogPost)
class DjangoBlogPostAdmin(admin.ModelAdmin):
    form = DjangoBlogAdminForm
    list_display = ['id','title']

@admin.register(MLBlogPost)
class MLBlogPostAdmin(admin.ModelAdmin):
    form = MLBlogAdminForm
    list_display = ['id','title']


@admin.register(DLBlogPost)
class MLBlogPostAdmin(admin.ModelAdmin):
    form = DLBlogAdminForm
    list_display = ['id','title']

@admin.register(AboutUs)
class MLBlogPostAdmin(admin.ModelAdmin):
    form = AboutUsAdminForm
    list_display = ['id']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email']