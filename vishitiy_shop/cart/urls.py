from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path("add/", views.CartAddView.as_view(), name="add"),
    path("update/", views.CartUpdateView.as_view(), name="update"),
    path("remove/", views.CartRemoveView.as_view(), name="remove"),
]

