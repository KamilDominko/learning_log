from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Nazwa użytkownika'
        self.fields['username'].help_text = 'Wprowadź nazwę użytkownika (do 150 znaków). Dozwolone litery, cyfry oraz znaki @/./+/-/_.'
        self.fields['password1'].label = 'Hasło'
        self.fields['password1'].help_text = 'Twoje hasło nie może być zbyt podobne do innych nazwy użytkownika.<br>Twoje hasło musi zawierać co najmniej 8 znaków.<br>Twoje hasło nie może być powszechnie używanym hasłem.<br>Twoje hasło nie może być w całości numeryczne.'
        self.fields['password2'].label = 'Potwierdź hasło'
        self.fields['password2'].help_text = 'Wprowadź ponownie hasło.'

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
