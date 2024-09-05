from django.urls import path
from . import views

urlpatterns =[
    path('user', views.Home),
    path('', views.get_blog),
    path('post', views.create_blog),
    path('update/<int:id>', views.update_blog),
    path('delete/<int:id>', views.delete_blog)    
]