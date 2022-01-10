from django.contrib import admin
from .models import PythonBlogPost, DjangoBlogPost
from .forms import PythonBlogAdminForm, DjangoBlogAdminForm


# Register your models here.

@admin.register(PythonBlogPost)
class PythonBlogPostAdmin(admin.ModelAdmin):
    form = PythonBlogAdminForm
    list_display = ['id','title']


@admin.register(DjangoBlogPost)
class PythonBlogPostAdmin(admin.ModelAdmin):
    form = DjangoBlogAdminForm
    list_display = ['id','title']
