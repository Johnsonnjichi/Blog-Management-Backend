from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import SignUp

urlpatterns =[
    # path('signup/', views.SignUp, name='signup'),
    # path('login/', views.LogIn, name='login'),
    path('login/', views.LogIn),
    path('signup/', views.SignUp),
    path('user', views.Home),
    path('', views.get_blog),
    path('post', views.create_blog),
    path('update/<int:id>', views.update_blog),
    path('delete/<int:id>', views.delete_blog),
    # path('signup/', signup, name='signup'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('signup/', views.signup),    
]