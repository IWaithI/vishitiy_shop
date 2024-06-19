from typing import Any
from django.shortcuts import render
from django.views import generic
from . models import Product
from django.db.models import QuerySet
from .filters import ProductFilter

# Create your views here.
class ProductListView(generic.ListView):
    # Здесь мы указываем шаблон который будет использоваться для отображения списка продуктов
    template_name = 'products/product_list.html'
    # Задаем queryset, который извлекает все объекты Product и использует select_related для оптимизации запросов
    queryset = Product.objects.all().select_related("collection")

    # метод для получения queryset 
    def get_queryset(self) -> QuerySet[Product]:
        # вызываем get_queryset из родительского класса для получения базового queryset
        qs = super().get_queryset()
        # Создаем экземпляр фильтра, передавая GET параметры запроса и базовый queryset
        self.filterset = ProductFilter(self.request.GET, queryset=qs)
        # Возвращаем отфильтрованный queryset
        return self.filterset.qs
    
    # Метод для получения контекста данных которые будут переданы в шаблон
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        # Получаем базовый контекст из родительского класса
        context = super().get_context_data(**kwargs)
        # Добавляем форму фильтра в контекст
        context["form"] = self.filterset.form
        # Возвращаем контекст
        return context


class ProductDetailView(generic.DetailView):
    # Задаем queryset, который извлекает все объекты Product и использует select_related для оптимизации запросов
    queryset = Product.objects.all().select_related("collection")
    # Указываем шаблон, который будет использоваться для отображения деталей продукта
    template_name = "products/product_detail.html"