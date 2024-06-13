
from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from .services.repository.ProdutoRepository import ProductModel
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from Ferteliz import settings
from core.models import ProductModel
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
            return HttpResponseRedirect('home')
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
            return HttpResponseRedirect('home')
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'login.html')

def cadastroVendedor(request):
    return render(request, 'cadastroVendedor.html') 

def carrinho(request):
    return render(request, 'carrinho.html') 

def cadastroProdutos(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            product = {
                'name': data.get('name'),
                'description': data.get('description'),
                'price': float(data.get('price'))
            }
            db = settings.db
            db.products.insert_one(product)
            return JsonResponse({'status': 'Produto cadastrado com sucesso!'})
        else:
            return JsonResponse({'status': 'Form não é válido.'}, status=400)
    else:
        form = ProductForm()
    return render(request, 'cadastroProdutos.html', {'form': form}) 

def homeCliente(request):
    return render(request, 'homeCliente.html') 

def homeVendedor(request):
    return render(request, 'homeVendedor.html')

def profileVendedor(request):
    return render(request, 'profileVendedor.html')

def profileCliente(request):
    return render(request, 'profileCliente.html')

def compras (request):
    return render(request, 'compras.html')

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
