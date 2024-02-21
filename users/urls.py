"""Definiuje wzorce adresów URL dla aplikacji users."""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Dołączenie domyślnych adresów URL uwierzytelniania.
    path('',include('django.contrib.auth.urls')),
]