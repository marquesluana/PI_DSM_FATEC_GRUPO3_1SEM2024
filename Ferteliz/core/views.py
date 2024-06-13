from django import db
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect

from .services.connection import get_db
from .services.repository.ProdutoRepository import ProductModel
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
from Ferteliz import settings
from core.models import UserModel, ProductModel
from .forms import UserForm, ProductForm
from django.contrib.auth.models import User
from django.conf import settings

# Create your views here.
def home (request):
    template_name = 'home.html'
    return render(request, template_name)

def cadastroMenu (request):
    template_name = 'cadastroMenu.html'
    return render(request, template_name)

def cadastroCliente(request):
    template_name = 'cadastroCliente.html'
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home')
            except Exception as e:
                # Capture qualquer exceção para diagnóstico
                messages.error(request, "Erro ao cadastrar usuário. Por favor, contate o suporte do sistema para assistência.")
                # Logar a exceção para ajudar no diagnóstico
                print(f"Erro ao cadastrar usuário: {e}")
        else:
            messages.error(request, "Erro no formulário. Por favor, verifique os campos e tente novamente.")
    
    else:
        form = UserForm()

    contexto = {'form': form}
    return render(request, template_name, contexto)

def login(request):
    template_name = 'login.html'
    # Obtenha a instância do banco de dados MongoDB
    
    if request.method == 'POST':
        cpf = request.POST['cpf']
        password = request.POST['password']

        # Autenticar o usuário manualmente
        user = db.users.find_one({"cpf": cpf, "password": password})
        if user:
            # Usar o User model do Django para login
            django_user = authenticate(request, username=cpf, password=password)
            if django_user is not None:
                auth_login(request, django_user)
                return redirect('home')
            else:
                # Criar um usuário Django se não existir
                django_user = User.objects.create_user(username=cpf, password=password)
                django_user.save()
                auth_login(request, django_user)
                return redirect('home')
        else:
            messages.error(request, 'CPF ou senha incorretos.')

    return render(request, template_name)

def logout(request):
    """Faz logout do usuário."""
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))

def cadastroVendedor(request):
    template_name = 'cadastroVendedor.html'
    return render(request, template_name) 

def carrinho(request):
    template_name = 'carrinho.html'
    return render(request, template_name) 

def cadastroProdutos(request):
    template_name = 'cadastroProdutos.html'
    return render(request, template_name) 

def homeCliente(request):
    template_name = 'homeCliente.html'
    return render(request, template_name) 

def homeVendedor(request):
    template_name = 'homeVendedor.html'
    return render(request, template_name)

def profileVendedor(request):
    template_name = 'profileVendedor.html'
    return render(request, template_name)

def profileCliente(request):
    template_name = 'profileCliente.html'
    return render(request, template_name)

def list_products(request):
    db = get_db()  # Obtém o banco de dados MongoDB
    produtos = list(db.products.find())  # Obtém todos os produtos e converte para uma lista Python

    context = {
        'produtos': produtos,
    }
    return render(request, 'list_products.html', context)

def add_product(request):
    template_name = 'add_product.html'
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'Produto cadastrado com sucesso!'})
        else:
            print(form.errors)  # Adicione esta linha para imprimir os erros do formulário no console
            errors = form.errors.as_json()
            return JsonResponse({'status': 'Formulário inválido', 'errors': errors}, status=400)
    else:
        form = ProductForm()
    return render(request, template_name, {'form': form})
