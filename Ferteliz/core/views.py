from bson import ObjectId
from django.shortcuts import render, HttpResponseRedirect
from .services.repository.ProdutoRepository import ProductModel
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, login as auth_login
from django.contrib.auth.decorators import login_required
from Ferteliz import settings
from core.models import ProductModel
from django.contrib.auth.models import User
from .forms import UserForm, ProductForm, EditUserForm
from django.http import HttpResponseRedirect



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
            login(request, user, backend='core.backends.CustomBackend')
            return HttpResponseRedirect('../homeCliente')
    else:
        form = UserForm()

    contexto = {'form': form}
    return render(request, 'cadastroCliente.html', contexto)

def user_login(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
        password = request.POST['password']
        user = authenticate(request, cpf=cpf, password=password)
        if user is not None:
            login(request, user, backend='core.backends.CustomBackend')
            return HttpResponseRedirect('../homeCliente')
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'login.html')

def cadastroVendedor(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='core.backends.CustomBackend')
            return HttpResponseRedirect('../homeVendedor')
    else:
        form = UserForm()

    contexto = {'form': form}
    return render(request, 'cadastroVendedor.html', contexto) 

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
            db = settings.get_mongo_client()
            db.produtos.insert_one(product)
            return JsonResponse({'status': 'Produto cadastrado com sucesso!'})
        else:
            return JsonResponse({'status': 'Form não é válido.'}, status=400)
            
    else:
        form = ProductForm()
    return render(request, 'cadastroProdutos.html', {'form': form}) 

def deletarProduto(request, produto_id):    
    db = settings.get_mongo_client()
    db.produtos.delete_one({'_id': ObjectId(produto_id)})
    return JsonResponse({'status': 'Produto deletado com sucesso!'})

def editarProdutos(request, produto_id):
    db = settings.get_mongo_client()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            # Atualiza o produto no MongoDB
            db.produtos.update_one({'_id': ObjectId(produto_id)}, {'$set': {
                'name': data.get('name'),
                'description': data.get('description'),
                'price': float(data.get('price'))
            }})
            return JsonResponse({'status': 'Produto atualizado com sucesso!'})
        else:
            return JsonResponse({'status': 'Form não é válido.'}, status=400)
            
    else:
        produto = db.produtos.find_one({'_id': ObjectId(produto_id)})    
        if produto:
            form = ProductForm(initial={
                'name': produto.get('name'),
                'description': produto.get('description'),
                'price': str(produto.get('price', ''))
            })       
    return render(request, 'editarProdutos.html', {'form': form}) 

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
    products = list(settings.get_mongo_client().produtos.find())
    data = []
    for product in products:
        data.append({
            'id' : str(product.get('_id', '')),
            'name': product.get('name', ''),
            'description': product.get('description', ''),
            'price': str(product.get('price', ''))
        })
    #return JsonResponse(data, safe=False)
    return render(request, 'list_products.html', {'products': data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            if request.user.tipo == 'cliente':
                return HttpResponseRedirect('../profileCliente')
            elif request.user.tipo == 'vendedor':
                return HttpResponseRedirect('../profileVendedor')
    else:
        form = EditUserForm(instance=request.user)
    
    return render(request, 'editPerfil.html', {'form': form})