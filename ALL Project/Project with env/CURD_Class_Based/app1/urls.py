from django.urls import path
from . import views

urlpatterns = [
    # path('',views.add_show, name="home"),
    path(route='', view=views.AddShowView.as_view(), name="home"),

    # path('delete/<int:id>/', views.delete_data, name="delete_info"),
    path(route='delete/<int:id>/', view=views.DeleteDataView.as_view(), name="delete_info"),

    # path('update/<int:id>/', views.update_data, name="update_info"),
    path(route='update/<int:id>', view=views.UpdateDataView.as_view(), name="update_info"),
    
]

