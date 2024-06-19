from django.shortcuts import render, redirect
# импортируем функцию render и redirect 
from django.urls import reverse_lazy
# Импортируем функцию reverse_lazy для создания URL-адресов на этапе выполнения
from django.contrib.auth import get_user_model
# Импортируем функцию get_user_model для получения модели пользователя
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Импортируем стандартные формы регистрации и аутентификации пользователей
from django.contrib.auth.views import LogoutView as DjangoLogoutView, LoginView as DjangoLoginView
# Импортируем стандартные представления выхода и входа в систему
from django.contrib import messages
# Импортируем модуль messages для отправки сообщений пользователю
from django.views import generic
# Импортируем модуль generic из django.views для создания обобщенных представлений
from . import forms
# Импортируем локальный модуль forms, который, вероятно, содержит кастомные формы регистрации и аутентификации


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
