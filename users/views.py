from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm


def register(request):
    """Rejestracja nowego użytkownika."""
    if request.method != 'POST':
        # Wyświetlenie pustego formularza rejestracji użytkownika.
        form = RegisterForm()
    else:
        # Przetworzenie wypełnionego formularza.
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')

    # Wyświetlenie pustego formularza.
    context = {'form': form}
    return render(request, 'registration/register.html', context)
