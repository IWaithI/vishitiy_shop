""" 
импортируем RangeWidget из библиотеки django_filters что бы использовать 
его как базовый класс для создания нашего пользовательского виджета 

"""
from django_filters.widgets import RangeWidget

# импортируем forms из Джанго
from django import forms


# Создание пользовательского виджета наследующегося от RangeWidget
class CustomRangeWidget(RangeWidget):
    #указываем шаблон где будем отображать данный виджет
    template_name = 'products/widgets/range.html'

    # Переопределение метода get_context для добавления дополнительного контекста
    def get_context(self, name, value, attrs):
        # Вызов метода get_context базового класса для получения начального контекста
        context = super().get_context(name, value, attrs)
        # Тут мы устанавливаем атрибуты min и max для виджета 
        context['widget']['attrs'] = {'min': self.attrs.get('min', 0), 'max': self.attrs.get('max', 5000)}
        # Интеграция по подвиджитами и суфиксами для установки дополнительных атрибутов
        for subcontext, suffix in zip(context["widget"]["subwidgets"], self.suffixes):
            #x-on:input="mintrigger"
            #x-model="minprice"
            # subcontext["attrs"][suffix+"length"] = len(str(context['widget']['attrs'][suffix]))

            # Установка атрибута x-on:input для каждого подвиджета, чтобы он вызывал соответствующее событие
            subcontext["attrs"]["x-on:input"] = suffix + "trigger"
            # Установка атрибута x:model для каждого подвиджета, чтобы он был связан с соотвецтвующей моделью
            subcontext["attrs"]["x-model"] = suffix + "price"
        # Возвращение изменённого контекста
        return context
