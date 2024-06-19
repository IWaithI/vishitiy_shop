## Vishitiy.ua - project
#### Our project is a online store for selling clothes
---

## Information about our team
1. GitHub - [Danil](https://github.com/danilgubarev)
2. GitHub - [Olha](https://github.com/Olhabd)
3. GitHub - [Oleksii](https://github.com/AlexeyTarasov77)
4. GitHub - [Vitalii](https://github.com/IWaithI)


## Technologies and languages we used
1. Python
2. Django
2. JavaScript
3. HTML
4. CSS
5. MySQL
6. Bootstrap



## Libraries we used

```txt

asgiref==3.8.1
# 
crispy-bootstrap5==2024.2
# Библиотека для совместимости Django с Bootstrap5, упрощает создания форм с использованием Bootstrap5
django-crispy-forms==2.1
# Приложение Джанго которое помогает создавать красивые формы
sqlparse==0.5.0
# парсер для работы с базами данных SQL
Pillow==10.3.0 
# Библиотека для работы с изображениями
django-colorfield==0.11.0 
# Библиотека которая используется для добавления "выбора цвета или цветовых полей" в моделях джанго
django-filter==24.2
# Библиотека которая позволяет легко создавать фильтры для данных в приложении
mysqlclient==2.2.4
# Джанго использует для подключения и работ с базами данных
faker==25.8.0 
# генерация потдельных данных 
python-dateutil==2.9.0.post0 
# библиотека для работыы с датами и временем
six==1.16.0
# Предназначен для потдержки баз кода, которые работают как на Python 2 так и на Python 3
python-dotenv==1.0.1
""" 
считывает ключ-значение с файла .env и
может устанавливать их как переменные
(У нас в проекте используется для хранения конфиденциальных данных) )

"""
algoliasearch==3.0.0 
# Официальная библиотека клиента Алголия для пайтона, используется для взаимодействия с поисковыми системами Алголии 
algoliasearch==django-3.0.0
# Библиотека для интеграции Алголии с Джанго
certifi==2024.6.2
# 
charset-normalizer==3.3.2
# Библиотека, которая помогает вам читать текст из неизвестной кодировки.
idna==3.7
# Используется для работы с URL-адресами, содержащими не-ASCII символы.
requests==2.32.3 
# Библиотека используемая для выполнения HTTP запросов
urllib3==2.2.1
# Библиотека для работы с HTTP
django-countries==7.6.1
# Библиотека для Джанго которая позволяет использовать список стран в моделях и формах
typing-extensions==4.12.2
# 

```





#### Function in users app:

1. __functions for registration login and logout:__

```python
User = get_user_model()  # Получаем модель пользователя, используя функцию get_user_model

# Функция представления для регистрации нового пользователя
def signup_view(request):
    form = UserCreationForm()  
    # Создаем экземпляр стандартной формы UserCreationForm для регистрации пользователя
    if request.method == "POST":  
       # Если запрос метода POST
       form = UserCreationForm(request.POST)  
       # Используем данные POST для создания формы UserCreationForm
       if form.is_valid():  
           # Если данные формы прошли валидацию
           form.save()  
           # Сохраняем пользователя
           messages.success(request, "Аккаунт был успешно создан")  
           # Отправляем сообщение об успешном создании аккаунта
           return redirect("users:login")  
       # Перенаправляем пользователя на страницу входа
    return render(request, "registration/signup.html", {"form": form})  
# Отображаем шаблон signup.html с формой для регистрации пользователя

# Функция представления для входа пользователя в систему
def login_view(request):
    form = AuthenticationForm()  
    # Создаем экземпляр стандартной формы AuthenticationForm для входа пользователя
    if request.method == "POST":  
        # Если запрос метода POST
        form = AuthenticationForm(data=request.POST)  
        # Используем данные POST для создания формы AuthenticationForm
        if form.is_valid():  
            # Если данные формы прошли валидацию
            user = form.get_user()  
            # Получаем пользователя из формы аутентификации
            messages.success(request, f"Вы вошли как {user.username}")  
            # Отправляем сообщение о успешном входе пользователя
    return render(request, "registration/login.html", {"form": form})  
# Отображаем шаблон login.html с формой для входа пользователя

# Класс для представления выхода пользователя из системы
class LogoutView(DjangoLogoutView):
    http_method_names = ["post", "options", "get"]  
    # Указываем допустимые HTTP методы для этого представления
    def get(self, *args, **kwargs):  
        # Определяем метод GET
        if not self.request.user.is_authenticated:  
            # Если пользователь не аутентифицирован
            return redirect("users:login")  
        # Перенаправляем его на страницу входа
        return render(self.request, "registration/logout.html")  
    # Отображаем шаблон logout.html

# Класс для представления входа пользователя в систему
class LoginView(DjangoLoginView):
    redirect_authenticated_user = True  
    # Перенаправляем аутентифицированного пользователя
    form_class = forms.CustomAuthenticationForm  
    # Используем кастомную форму аутентификации CustomAuthenticationForm
    def form_valid(self, form):  
        # Переопределяем метод для обработки валидной формы
        messages.success(self.request, f"Вы вошли как {form.get_user().username}")  
        # Отправляем сообщение о успешном входе пользователя
        return super().form_valid(form)  
    # Вызываем родительский метод form_valid

# Класс для представления регистрации нового пользователя с использованием обобщенного представления CreateView
class SignupView(generic.CreateView):
    form_class = forms.CustomUserCreationForm  
    # Используем кастомную форму регистрации CustomUserCreationForm
    success_url = reverse_lazy("users:login")  
    # После успешной регистрации перенаправляем пользователя на страницу входа
    template_name = "registration/signup.html"  
    # Определяем имя шаблона для отображения формы регистрации
    def form_valid(self, form):  
        # Переопределяем метод для обработки валидной формы
        messages.success(self.request, "Аккаунт был успешно создан")  
        # Отправляем сообщение об успешной регистрации аккаунта
        return super().form_valid(form)  
    # Вызываем родительский метод form_valid для сохранения данных формы

```
_Этот код содержит представления для регистрации входа и выхода пользователя для этого мы использовали стандартные Джанго формы так же сдесь используем кастомные формы которы находятся в файле forms.py_

---

2.__Creat customs forms:__

```python

# создание кастомной формы аунтефикации наследующуюся от стандартных форм Джанго
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        # Вызов родительского конструктора что бы инициализировать форму
        super().__init__(*args, **kwargs)
        # Если в данных формы ('self.data') есть поле password
        if 'password' in self.data:
            # Устанавливаем атрибут value виджета поля password равным значению из данных формы
            self.fields['password'].widget.attrs['value'] = self.data['password']

# создаём кастомную форму создания пользователя наследующуюся от стандартной формы создания пользователя Джанго
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        # Вызов родительского конструктора что бы инициализировать форму
        super().__init__(*args, **kwargs)
        # Если в данных формы ('self.data') есть поле password1
        if 'password1' in self.data:
            # Устанавливаем атрибут 'value' виджета поля 'password1' равным значению из данных формы
            self.fields['password1'].widget.attrs['value'] = self.data['password1']
        # Если в данных формы ('self.data') есть поле password2
        if 'password2' in self.data:
            # Устанавливаем атрибут value виджета поля password2 равным значению из данных формы
            self.fields['password2'].widget.attrs['value'] = self.data['password2']

```

_Эти кастомные формы позволяют сохранять введённые пароли пользователем при перезагрузке страницы_

---


#### Function in the products app:

1. __Отображение списка продуктов, а так же деталей продуктов(личная страница продукта)__

```python 
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

```

_Объяснение кода_

* ProductListView - отображает весь список продуктов с использованием фильтрации

* ProductDetailView - отображает личную страницу товара 

_Классы используются с Django для управления представлениями generic.ListView и generic.DetailView которые обеспечивают отображение списка и "детали" продукта модели Product_

* generic.ListView - нам нужен для отображения списка объектов модели в Django

* generic.DetailView - нам нужен для отображения деталей продукта(Личной страницы)

---

2. Создание моделей Product и Collection

```python

from django.core.validators import MinValueValidator, MaxValueValidator  
# Импортируем валидаторы для минимального и максимального значений
from django.db import models  
# Импортируем модуль моделей Django
from django.urls import reverse  
# Импортируем функцию reverse для построения URL
from main.mixins import SaveSlugMixin  
# Импортируем миксин для автоматического сохранения slug
from products.validators import ProductSizeValidator  
# Импортируем валидатор размера продукта

class Product(SaveSlugMixin, models.Model):  
    # Определяем модель Product, наследующую SaveSlugMixin и models.Model
    ACCEPTABLE_SIZES = ["XS", "S", "M", "L", "XL", "XXL"]  
    # Допустимые размеры продукта
    SIZE_CHOICES = tuple((size, size) for size in ACCEPTABLE_SIZES)  
    # Создаём кортеж с вариантами размеров для выбора
    COLOR_PALETTE = tuple((color, color) for color in ("white", "black", "red", "green", "blue", "yellow"))  
    # Цветовая палитра
    PRODUCT_TYPE_CHOICES = tuple(
        (type, type)
        for type in ("shoes", "t-shirt", "sweatshirt", "pants", "jacket", "sunglasses")  # Варианты типов продуктов
    )
    
    SIZE_VALIDATOR = ProductSizeValidator(ACCEPTABLE_SIZES)  
    # Создаём экземпляр валидатора размеров
    
    title = models.CharField(max_length=150)  
    # Поле для названия продукта
    slug = models.SlugField(unique=True, blank=True)  
    # Поле для slug, уникальное и может быть пустым
    available_colors = models.JSONField(default=list)  
    # Поле для доступных цветов, используется JSON
    available_sizes = models.JSONField(default=list, validators=[SIZE_VALIDATOR.validate_size])  
    # Поле для доступных размеров, используется JSON с валидатором
    available = models.BooleanField(default=True)  
    # Поле для статуса доступности продукта
    type = models.CharField(choices=PRODUCT_TYPE_CHOICES, max_length=50)  
    # Поле для типа продукта с ограниченным выбором
    image = models.ImageField()  
    # Поле для изображения продукта
    description = models.TextField(blank=True, null=True)  
    # Поле для описания продукта, может быть пустым или null
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    # Поле для цены продукта
    discount = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]  
        # Поле для скидки с валидаторами минимального и максимального значений
    )
    collection = models.ForeignKey(
        "Collection", on_delete=models.CASCADE, related_name="products"  
        # Поле внешнего ключа, связывает продукт с коллекцией
    )

    def __str__(self) -> str:
        return self.title  
    # Метод для строкового представления объекта
    
    @property
    def image_url(self):
        return self.image.url  
    # Свойство для получения URL изображения
    
    @property
    def final_price(self):
        return self.price - (self.price * self.discount / 100)  
    # Свойство для вычисления окончательной цены с учётом скидки

    @property
    def url(self):
        return self.get_absolute_url()  
    # Свойство для получения абсолютного URL продукта
    
    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})  
    # Метод для получения абсолютного URL продукта
    
    def save(self, *args, **kwargs) -> None:
        return super().save(slugify_value=self.title, *args, **kwargs)  
    # Метод сохранения объекта с автоматическим генерацией slug

class Collection(SaveSlugMixin, models.Model):  
    # Определяем модель Collection, наследующую SaveSlugMixin и models.Model
    name = models.CharField(max_length=150)  
    # Поле для названия коллекции
    slug = models.SlugField(unique=True, blank=True)  
    # Поле для slug, уникальное и может быть пустым
    image = models.ImageField()  
    # Поле для изображения коллекции
    description = models.TextField(blank=True, null=True)  
    # Поле для описания коллекции, может быть пустым или null

    def __str__(self) -> str:
        return self.name  
    # Метод для строкового представления объекта

    def save(self, *args, **kwargs) -> None:
        return super().save(slugify_value=self.name, *args, **kwargs)  
    # Метод сохранения объекта с автоматическим генерацией slug

```

_Этот код используется для работы с Коллекциями и Личной страницы товара предоставляя удобные методы доступа, сохранения и связывания данных в базе данных_

* @property - позволяет представлять метод как свойство объекта


___


3. Фильтрация данных на странице

```python

# Определяем класс фильтра для модели Product
class ProductFilter(django_filters.FilterSet):
    # Фильтр для цены с использованием кастомного виджета диапазона цен
    price = django_filters.RangeFilter(widget=CustomRangeWidget(attrs={'class': 'px-3 py-2 border border-gray-200 rounded w-24 text-center'}))
    
    # Фильтр для размера с использованием виджета множественного выбора с чекбоксами
    size = django_filters.TypedMultipleChoiceFilter(
        field_name="available_sizes",  # Поле модели, по которому будет фильтрация
        choices=Product.SIZE_CHOICES,  # Доступные варианты размеров
        widget=forms.CheckboxSelectMultiple,  # Виджет для отображения вариантов в виде чекбоксов
        lookup_expr='icontains'  # Метод поиска (независимый от регистра поиск в строках)
    )
    
    # Фильтр для коллекции с использованием виджета множественного выбора с чекбоксами
    collection = django_filters.ModelMultipleChoiceFilter(
        queryset=Collection.objects.all(),  # Все объекты коллекции
        widget=forms.CheckboxSelectMultiple  # Виджет для отображения вариантов в виде чекбоксов
    )
    
    # Фильтр для цвета с использованием виджета множественного выбора с чекбоксами
    color = django_filters.TypedMultipleChoiceFilter(
        field_name='available_colors',  # Поле модели, по которому будет фильтрация
        choices=Product.COLOR_PALETTE,  # Доступные варианты цветов
        widget=forms.CheckboxSelectMultiple,  # Виджет для отображения вариантов в виде чекбоксов
        lookup_expr='icontains'  # Метод поиска (независимый от регистра поиск в строках)
    )
    
    # Фильтр для отображения только товаров со скидкой
    discounted_only = django_filters.BooleanFilter(
        field_name="discount",  # Поле модели, по которому будет фильтрация
        label="Discounted only",  # Метка для фильтра
        widget=forms.CheckboxInput,  # Виджет для отображения в виде чекбокса
        method='filter_discounted_only'  # Метод фильтрации
    )
    
    # Метод фильтрации, который возвращает только товары со скидкой, если чекбокс выбран
    def filter_discounted_only(self, queryset, name, value):
        if value:  # Если чекбокс выбран
            return queryset.filter(discount__gt=0)  # Возвращаем товары с ненулевой скидкой
        return queryset  # Иначе возвращаем все товары

    # Мета-класс для указания модели и полей, которые будут использоваться для фильтрации
    class Meta:
        model = Product  # Указываем модель, для которой создается фильтр
        fields = ["price", "discounted_only", "type", "size", "color", "collection"]  # Поля модели, которые будут использоваться для фильтрации


```

_Этот код проводит фильтрацию на странице по различным параметрам, таких как цена, тип продукта, размер, цвеет, коллекция и т.д_

___


3. Кастомизация админ панели)

```python

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

```


_С помощью этого кода проводим кастомизацию админ панели_

* Здесь используется декоратор admin.register, чтобы зарегистрировать модель Product и связать её с кастомным классом ProductAdmin, который наследуется от admin.ModelAdmin.





