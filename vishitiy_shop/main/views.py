from django.shortcuts import render
from django.http import JsonResponse
from products.models import Collection
from dotenv import load_dotenv
import os

load_dotenv()

# Create your views here.

# Главная функция отображения всей главной страницы
def main_view(request):
    # получение коллекций из модели
    collections = Collection.objects.all()
    # отображаем шаблон с коллекциями
    return render(request, "main/index.html", {"collections": collections})

# Получение учётных данных с Algolia
def get_algolia_credentials(request):
    # возвращаем данные для Algolia в формате JSON
    return JsonResponse({
        # Информацию получаем из файла .env 
        "APP_ID": os.getenv("ALGOLIA_APP_ID"),
        "API_KEY": os.getenv("ALGOLIA_API_KEY")
    })