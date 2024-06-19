from django.urls import path  
# Импортируем функцию path для создания URL-правил
from . import views  
# Импортируем views из текущего приложения

app_name = 'products'  
# Устанавливаем пространство имён для URL-адресов этого приложения

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),  
    # URL для списка продуктов. Путь '' указывает на корневой URL.
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='detail'),  
    # URL для деталей продукта. Путь содержит параметр 'slug'.
]