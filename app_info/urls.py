from django.urls import path
from . import views

urlpatterns = [
    path('users/dashboard/', views.user_dashboard, name="user_dashboard"),
    path('users/register/', views.user_register, name = "user_register"),
    path('users/login/', views.user_login, name = "user_login"),


]
