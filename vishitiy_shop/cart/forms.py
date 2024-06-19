from .cart import Cart  # Импорт класса Cart для работы с корзиной
from django import forms  # Импорт модуля форм Django
from products.validators import ProductSizeValidator  # Импорт валидатора размеров продуктов
from products.models import Product  # Импорт модели Product

class CartBaseForm(forms.Form):
    # Базовый класс формы для работы с корзиной.

    def process_request(self, request):
        # Метод для обработки запроса. Устанавливает атрибут request.
        print("CALLING METHOD", request)
        self.request = request

    def save(self):
        # Метод сохранения. Проверяет валидность формы и наличие запроса.
        assert self.is_valid(), 'Form is not valid'
        assert self.request, 'Request is not provided'

class CartAddForm(CartBaseForm):
    # Форма для добавления продукта в корзину.

    product_id = forms.CharField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(initial=1, min_value=1, required=False)
    size = forms.CharField(validators=[ProductSizeValidator(Product.ACCEPTABLE_SIZES).validate_size])
    color = forms.CharField()
    price = forms.DecimalField()
    
    def clean(self):
        # Метод очистки данных формы проверяет, что продукт еще не добавлен в корзину.
        if getattr(self, 'request', None):
            cart = Cart(self.request)
            if self.cleaned_data['product_id'] in cart:
                raise forms.ValidationError('Продукт вже знаходиться в корзині')
        return self.cleaned_data

    def save(self):
        # Переопределенный метод сохранения. Вызывает базовый метод сохранения и добавляет продукт в корзину.
        super().save()
        self.cleaned_data['price'] = str(self.cleaned_data['price'])
        cart = Cart(self.request)
        return cart.add(**self.cleaned_data)
            

class CartUpdateForm(CartAddForm):
    # Форма для обновления количества продукта в корзине.

    def __init__(self, *args, **kwargs):
        # Конструктор класса. Изменяет поведение полей формы.
        super().__init__(*args, **kwargs)
        del self.fields['final_price']  # Удаляет поле final_price из формы
        for field in self.fields.values():
            field.required = False  # Устанавливает все поля формы как необязательные
        self.fields['product_id'].required = True  # Устанавливает поле product_id как обязательное
        
    def save(self):
        # Переопределенный метод сохранения. Обновляет количество продукта в корзине.
        cart = Cart(self.request)
        return cart.update(**self.cleaned_data)
        
        
class CartRemoveForm(CartBaseForm):
    # Форма для удаления продукта из корзины.

    product_id = forms.CharField(widget=forms.HiddenInput)
    
    def clean(self):
        # Метод очистки данных формы. Проверяет, что продукт присутствует в корзине.
        if getattr(self, 'request', None):
            cart = Cart(self.request)
            if self.cleaned_data['product_id'] not in cart:
                raise forms.ValidationError('Цього продукту немає в вашiй корзині')
        return self.cleaned_data

    def save(self):
        # Переопределенный метод сохранения. Удаляет продукт из корзины.
        cart = Cart(self.request)
        return cart.remove(**self.cleaned_data)