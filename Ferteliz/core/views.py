from django.shortcuts import render, redirect, HttpResponseRedirect
from .services.repository.ProdutoRepository import ProductModel
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.urls import reverse
from Ferteliz import settings
from core.models import UserModel, ProductModel
from .forms import UserForm, ProductForm

# Create your views here.
def home (request):
    return render(request, 'home.html')

def cadastroMenu (request):
    return render(request, 'cadastroMenu.html')

def cadastroCliente(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = UserForm()
        contexto = {'form': form}
        return render(request, 'cadastroCliente.html', contexto)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def cadastroVendedor(request):
    return render(request, 'cadastroVendedor.html') 

def carrinho(request):
    return render(request, 'carrinho.html') 

def cadastroProdutos(request):
    return render(request, 'cadastroProdutos.html') 

def homeCliente(request):
    return render(request, 'homeCliente.html') 

def homeVendedor(request):
    return render(request, 'homeVendedor.html')

def profileVendedor(request):
    return render(request, 'profileVendedor.html')

def profileCliente(request):
    return render(request, 'profileCliente.html')

def list_products (request):
    products = ProductModel.objects.all()
    data = []
    for product in products:
        data.append({
            'name': product.name,
            'description': product.description,
            'price': str(product.price)
        })
    return JsonResponse(data, safe=False)
    #return render(request, 'list_products.html')

def add_product(request):
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
    return render(request, 'add_product.html', {'form': form})


