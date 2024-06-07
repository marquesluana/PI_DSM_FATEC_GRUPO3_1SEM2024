from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login

from Ferteliz import settings
from .models import Product
from .forms import UserForm, ProductForm

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'core/register.html', {'form': form})

def list_products(request):
    products = Product.objects.all()
    data = []
    for product in products:
        data.append({
            'name': product.name,
            'description': product.description,
            'price': str(product.price)  # Convertendo para string para garantir compatibilidade com JSON
        })
    return JsonResponse(data, safe=False)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Se salvar no Django ORM:
            # form.save()

            # Salvando diretamente no MongoDB:
            data = form.cleaned_data
            product = {
                'name': data.get('name'),
                'description': data.get('description'),
                'price': float(data.get('price'))
            }
            db = settings.db
            db.products.insert_one(product)
            return JsonResponse({'status': 'Product added successfully'})
        else:
            return JsonResponse({'status': 'Form is not valid'}, status=400)
    else:
        form = ProductForm()
    return render(request, 'core/add_product.html', {'form': form})
