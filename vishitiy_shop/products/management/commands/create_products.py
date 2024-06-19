import random 
 # Импортируем модуль random для генерации случайных данных

from django.core.management.base import BaseCommand  
# Импортируем BaseCommand для создания пользовательских команд Django
from django.conf import settings  
# Импортируем настройки из конфигурации Django
from faker import Faker  
# Импортируем Faker для генерации фейковых данных
from products.models import Collection, Product  
# Импортируем модели Django

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()  
        # Создаем экземпляр Faker для генерации фейковых данных
        
        # Цикл для создания 10 фейковых объектов Collection
        for _ in range(10):
            Collection.objects.create(
                name=fake.name(),  # Генерируем фейковое название для коллекции
                image=fake.image_url(),  # Генерируем фейковый URL изображения для коллекции
                description=fake.text(),  # Генерируем фейковое описание для коллекции
            )
            
            # Создаем объект Product
            Product.objects.create(
                title=fake.name(),  # Генерируем фейковое название для продукта
                available_colors=random.sample([color[0] for color in Product.COLOR_PALETTE], 3),  # Выбираем случайные цвета из COLOR_PALETTE
                available_sizes=random.sample(Product.ACCEPTABLE_SIZES, 3),  # Выбираем случайные размеры из ACCEPTABLE_SIZES
                type=random.choice(Product.PRODUCT_TYPE_CHOICES)[0],  # Выбираем случайный тип продукта из PRODUCT_TYPE_CHOICES
                image="collection_ex.png",  # Заглушка для изображения продукта
                description=fake.text(),  # Генерируем фейковое описание для продукта
                price=fake.random_int(min=100, max=5000),  # Генерируем случайную цену от 100 до 5000
                collection=random.choice(Collection.objects.all()),  # Связываем продукт с случайной коллекцией
            )