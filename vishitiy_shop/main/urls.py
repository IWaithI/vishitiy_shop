from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # урл для отображения главной страницы
    path('', views.main_view, name='index'),
    # урл для получения данных с Алголии
    path("get_algolia_credentials/", views.get_algolia_credentials, name="get_algolia_credentials"),
]