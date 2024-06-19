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
