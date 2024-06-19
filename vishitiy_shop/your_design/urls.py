from django.urls import path
from . import views

app_name = 'your_design'

urlpatterns = [
    path('', views.design_page, name='design'),
]