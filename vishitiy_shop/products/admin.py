from django.contrib import admin  # Импортируем модуль admin из Django для регистрации моделей в админ-панели
from django import forms  # Импортируем модуль forms из Django для создания форм

from .models import Collection, Product  # Импортируем модели Collection и Product

# Регистрируем модель Collection в админ-панели
admin.site.register(Collection)

# Регистрируем модель Product с использованием кастомного класса ProductAdmin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в списке продуктов в админ-панели
    list_display = ["title", "final_price", "collection", "available"]
    
    # Переопределяем метод get_form для кастомизации формы редактирования продукта
    def get_form(self, request, obj=None, **kwargs):
        # Получаем базовую форму для модели Product
        form = super().get_form(request, obj, **kwargs)
        
        # Кастомизируем виджет для поля available_sizes
        form.base_fields['available_sizes'].widget = forms.CheckboxSelectMultiple(
            choices=Product.SIZE_CHOICES,  # Устанавливаем возможные варианты выбора размеров
            attrs={'class': 'form-control'},  # Добавляем CSS-класс для оформления
        )
        
        # Кастомизируем виджет для поля available_colors
        form.base_fields['available_colors'].widget = forms.CheckboxSelectMultiple(
            choices=Product.COLOR_PALETTE,  # Устанавливаем возможные варианты выбора цветов
            attrs={'class': 'form-control'}  # Добавляем CSS-класс для оформления
        )
        
        # Возвращаем кастомизированную форму
        return form