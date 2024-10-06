from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Project, Experiencia
from .forms import ProjectForm, ExperienciaForm


def home(request):
    projects = Project.objects.all()
    user = request.user
    return render(request, "home.html", {
        "projects": projects,
        'user': user
        })

# Registro: 

def signup(request):
    if request.method == 'GET':
        return render(request, "signup.html", {
            'form': UserCreationForm
        })
    else: 
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                return render(request, "signup.html", {
                    'form': UserCreationForm,
                    "error": "El nombre de usuario ya ha sido tomado. Por favor, elige otro nombre."
                    })
        else:
            return render(request, "signup.html", {
                'form': UserCreationForm,
                "error": "Las contraseñas no coinciden."
                })
        

# Cerrar sesión:

def signout(request):
    logout(request)
    return redirect('home')

# Iniciar sesión:
def signin(request):
    if request.method == 'GET':
        return render(request, "signin.html", {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "signin.html", {
                'form': AuthenticationForm,
                "error": "Nombre de usuario y/o contraseña incorrectos."
            })
        else:
            login(request, user)
            return redirect("home")
        

@login_required
def create_project(request):
    if request.method == 'GET':
        return render(request, "create_project.html", {
            'form': ProjectForm
        })
    else:
        
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.user = request.user
            new_project.save()
            return redirect("home")
        else: 
            return render(request, "create_project.html", {
                'form': ProjectForm,
                "error": "Los datos que ingresaste son incorrectos. Por favor, inténtalo de nuevo."
            })
