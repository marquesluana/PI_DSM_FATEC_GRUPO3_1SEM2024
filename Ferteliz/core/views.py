
from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, 'home.html')

def cadastroMenu (request):
    return render(request, 'cadastroMenu.html')

def login (request):
    return render(request, 'login.html')

def cadastroCliente (request):
    return render(request, 'cadastroCliente.html')

def cadastroVendedor (request):
    return render(request, 'cadastroVendedor.html')