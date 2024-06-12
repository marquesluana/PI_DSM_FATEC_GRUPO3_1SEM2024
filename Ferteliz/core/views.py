
from django.shortcuts import render
from .services.repository.ProdutoRepository import ProductModel



# Create your views here.
def home (request):
    return render(request, 'home.html')

def cadastroMenu (request):
    return render(request, 'cadastroMenu.html')

def cadastroCliente(request):
    return render(request, 'cadastroCliente.html') 

def login(request):
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

def add_product (request):
    
    
    return render(request, 'add_product.html')

def list_products (request):
    return render(request, 'list_products.html')