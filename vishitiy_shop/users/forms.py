from django import forms 
# Импортируем модуль фоорм джанго
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Иммпортируем стандартные формы аутентификации и создания пользователя из джанго

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