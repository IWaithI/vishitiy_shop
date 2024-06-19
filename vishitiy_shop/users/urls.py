from django.urls import path 
# Импортируем функцию path для создания маршрутов URL
from django.contrib.auth import views as auth_views
# 
from . import views
# Импортируем представления из текущей дирретории

app_name = 'users'
# определяем пространство имён дял маршрутов данного приложения

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    # URL для страницы входа в систему, использует кастомное представление LoginView
    path('signup/', views.SignupView.as_view(), name='signup'),
    # URL для регистрации, использует кастомное представление SignupView
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # URL для выхода из аккаунта, использует кастомное представление LogoutView
]