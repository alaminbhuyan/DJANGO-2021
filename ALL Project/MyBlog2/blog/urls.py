from django.urls import path 
from . import views


urlpatterns = [
    path(route='', view=views.HomeTemplateView.as_view(), name='home'),

    path(route='pythonBlog/', view=views.PythonBlogListView.as_view(), name='pythonBlog'),

    # path(route='pythonSingle_post/<int:pk>', view=views.PythonBlogDetailView.as_view(), name='pythonSingle_post'),
    # path(route='pythonSingle_post/<str:slug>', view=views.PythonBlogDetailView.as_view(), name='pythonSingle_post'),

    path(route='pythonSingle_post/<str:slug>', view=views.PythonSingleBlog, name='pythonSingle_post'),
    path(route='postComment/', view=views.PythonpostComment, name='postComment'),
    #-------------------------------------------------------------------------------------------------------------
    path(route='djangoBlog/', view=views.DjangoBlogListView.as_view(), name='djangoBlog'),

    # path(route='DjangoSingle_post/<int:pk>', view=views.DjangoBlogDetailView.as_view(), name='DjangoSingle_post'),
    # path(route='DjangoSingle_post/<str:slug>', view=views.DjangoBlogDetailView.as_view(), name='DjangoSingle_post'),

    path(route='DjangoSingle_post/<str:slug>', view=views.DjangoSingleBlog, name='DjangoSingle_post'),
    path(route='DjangopostComment/', view=views.DjangopostComment, name='DjangopostComment'),
    #-------------------------------------------------------------------------------------------------------------
    path(route='MLBlog/', view=views.MLBlogListView.as_view(), name='MLBlog'),


    # path(route='MLSingle_post/<int:pk>', view=views.MLBlogDetailView.as_view(), name='MLSingle_post'),
    # path(route='MLSingle_post/<str:slug>', view=views.MLBlogDetailView.as_view(), name='MLSingle_post'),

    path(route='MLSingle_post/<str:slug>', view=views.MLSingleBlog, name='MLSingle_post'),
    path(route='MLpostComment/', view=views.MLpostComment, name='MLpostComment'),

    #-------------------------------------------------------------------------------------------------------------

    path(route='DLBlog/', view=views.DLBlogListView.as_view(), name='DLBlog'),

    # path(route='DLSingle_post/<int:pk>', view=views.DLBlogDetailView.as_view(), name='DLSingle_post'),
    # path(route='DLSingle_post/<str:slug>', view=views.DLBlogDetailView.as_view(), name='DLSingle_post'),

    path(route='DLSingle_post/<str:slug>', view=views.DLSingleBlog, name='DLSingle_post'),
    path(route='DLpostComment/', view=views.DLpostComment, name='DLpostComment'),

    #-------------------------------------------------------------------------------------------------------------

    path(route='randomBlogPost/', view=views.RandomBlopPostTemplateView.as_view(), name='randomBlogPost'),

    path(route='about/', view=views.AboutTemplateView.as_view(), name='about'),
    path(route='contact/', view=views.ContactFormView.as_view(), name='contact'),
    path(route='search/', view=views.postSearch, name='search'),

]
