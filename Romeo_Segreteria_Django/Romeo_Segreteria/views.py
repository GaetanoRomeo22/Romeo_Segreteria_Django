from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
def login_view(request):  # View per il form di login
    if request.method == 'POST':
        username = request.POST.get('username') # Estrae l'username dalla richiesta
        password = request.POST.get('password') # Estrae la password dalla richiesta
        user = authenticate(request, username=username, password=password) # Autentica l'utente
        if user is not None: # Se l'utente è autenticato
            login(request, user)
            return redirect('account') # Indirizza l'utente all'area riservata
        else: # Se l'utente non è autenticato
            messages.error(request, 'Credenziali incorrette')
    return render(request, 'login.html') # Indirizza l'utente alla pagina di login


def account_view(request):  # View per l'area riservata
    return render(request, 'account.html')


def register_view(request):  # View per il form di registrazione
    return render(request, 'registrazione.html')


def forgot_password_view(request):  # View per il form di recupero password
    return render(request, 'recupero_password.html')