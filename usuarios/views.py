from django.shortcuts import render, redirect

# contrib, pasta com apps já instalados (auth), de autenticação,
# e de models, onde ficam as tabelas do bd, importe a tabela User.
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.messages import constants
from django.contrib import messages


# Create your views here.
# Processar os dados.

# Mensagens


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        users = User.objects.filter(username = username)

        if users.exists():
            print("Erro 1")
            return redirect('/usuarios/cadastro')

        if senha != confirmar_senha:
            print("Erro 2")
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve possuir pelo menos 6 caracteres')
            return redirect("/usuarios/cadastro")

        try:
            User.objects.create_user(
                username = username,
                email = email,
                password = senha
            )
            return redirect('/usuarios/cadastro')
        except:
            print("Erro 4")
            return redirect('/usuarios/cadastro')
        
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get("senha")
        user = auth.authenticate(request, username=username, password=senha)
        
        if user:
            auth.login(request, user)
            return redirect('/pacientes/home')
        
        messages.add_message(request, constants.ERROR, 'Usuário ou senha incorretos')
        return redirect('/usuarios/login')
    
def sair(request):
    auth.logout(request)
    return redirect('/usuarios/login')

