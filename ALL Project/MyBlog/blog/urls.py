from django.urls import path 
from . import views


urlpatterns = [
    # path(route='', view=views.home, name='home'),
    path(route='', view=views.HomeTemplateView.as_view(), name='home'),

    # path(route='pythonBlog/', view=views.pythonBlog, name='pythonBlog'),
    path(route='pythonBlog/', view=views.PythonBlogListView.as_view(), name='pythonBlog'),

    path(route='single_post/<int:pk>', view=views.PythonBlogDetailView.as_view(), name='single_post'),

    # path(route='djangoBlog/', view=views.djangoBlog, name='djangoBlog'),
    path(route='djangoBlog/', view=views.DjangoBlogListView.as_view(), name='djangoBlog'),

    path(route='MLBlog/', view=views.MLBlog, name='MLBlog'),
    
    path(route='DLBlog/', view=views.DLBlog, name='DLBlog'),
]
