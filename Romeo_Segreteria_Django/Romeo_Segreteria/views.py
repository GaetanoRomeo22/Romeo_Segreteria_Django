from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
def login_view(request):  # View per il form di login
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, 'Credenziali incorrette')
    return render(request, 'login.html')


def account_view(request):  # View per l'area riservata
    return render(request, 'account.html')


def register_view(request):  # View per il form di registrazione
    return render(request, 'registrazione.html')


def forgot_password_view(request):  # View per il form di recupero password
    return render(request, 'recupero_password.html')


from django.shortcuts import render

# Create your views here.
