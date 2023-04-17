from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })

def about(request):
    return render(request, 'mainapp/index.html', {
        'title': 'Sobre nosotros'
    })

def register_page(request):

    # Validamos autenticacion
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        # Enviamos informacion del formulario
        if request.method == 'POST':
            register_form = RegisterForm(request.POST) # RegisterForm, es el formulario personalizado. UserCreationForm, es el formulario por defecto

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Te has registrado correctamente')
                return redirect('inicio')
        else:
            # Obtenemos formulario de registro
            register_form = RegisterForm() # RegisterForm, es el formulario personalizado. UserCreationForm, es el formulario por defecto

        # Mostramos formulario
        return render(request, 'users/register.html', {
            'title': 'Registro',
            'register_form': register_form
        })

def login_page(request):

    # Validamos autenticacion
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        # Enviamos informacion del formulario
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Pasamos informacion en keywords arguments
            user = authenticate(request, username=username, password=password)

            # Validamos autenticacion
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.warning(request, 'No te has identificado correctamente :(')

        # Mostramos formulario
        return render(request, 'users/login.html', {
            'title': 'Identifícate'
        })

def logout_user(request):
    logout(request)
    return redirect('login')
