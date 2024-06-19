from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.email_form, name='email'),
]