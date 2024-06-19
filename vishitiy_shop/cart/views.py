from typing import Any  # Импорт для поддержки типизации Any
from django.views import generic  # Импорт общих классов представлений Django
from django.views.generic.edit import FormMixin  # Импорт для поддержки форм в представлениях
from django.http import HttpRequest, HttpResponse, JsonResponse  # Импорт для работы с HTTP запросами и ответами
from . import forms  # Импорт локальных форм, определенных в текущем приложении

class CartMixin(FormMixin, generic.View):
    
    # Миксин для работы с корзиной, реализующий добавление, обновление и удаление товаров.
    
    status_code = 200  # Код состояния HTTP ответа по умолчанию
    msg = None  # Сообщение, которое будет отправлено в ответе

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        
        # Обработчик POST запроса для добавления, обновления или удаления товара из корзины.
      
        form = self.get_form()  # Получаем экземпляр формы
        form.process_request(request)  # Обрабатываем запрос формой
        if form.is_valid():  # Проверяем валидность данных формы
            return self.form_valid(form)  # Если данные формы валидны, вызываем метод form_valid
        else:
            return self.form_invalid(form)  # Если данные формы невалидны, вызываем метод form_invalid

    def form_valid(self, form: Any) -> HttpResponse:
       
        # Метод вызывается при успешной валидации формы.
       
        saved_data = form.save() or {}  # Сохраняем данные из формы, если форма поддерживает метод save
        return JsonResponse({'data': saved_data, 'msg': self.msg}, status=self.status_code)  # Возвращаем JSON ответ с данными и сообщением

    def form_invalid(self, form: Any) -> HttpResponse:
       
       # Метод вызывается при ошибке валидации формы.
      
        return JsonResponse({'msg': 'Ошибка валидации', 'errors': form.errors}, status=422)  # Возвращаем JSON ответ с сообщением об ошибке валидации и ошибками формы

class CartAddView(CartMixin):

    # Представление для добавления товара в корзину.
    
    form_class = forms.CartAddForm  # Указываем класс формы для добавления товара
    msg = 'Товар додано до кошика'  # Сообщение об успешном добавлении товара

class CartUpdateView(CartMixin):
    
    # Представление для обновления количества товара в корзине.
   
    form_class = forms.CartUpdateForm  # Указываем класс формы для обновления количества товара
    msg = 'Кількість змінено'  # Сообщение об успешном обновлении количества товара

class CartRemoveView(CartMixin):
   
    # Представление для удаления товара из корзины.
    
    form_class = forms.CartRemoveForm  # Указываем класс формы для удаления товара
    status_code = 204  # Код состояния HTTP ответа для успешного удаления товара