from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login
from django.urls import reverse
from Ferteliz import settings
from core.models import UserModel, ProductModel
from .forms import UserForm, ProductForm

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    return HttpResponseRedirect(reverse('home'))

def register(request):
    print(request)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            UserModel.objects.create(**form.cleaned_data)
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(reverse('home'))
    else:
        form = UserForm()
        contexto = {'form': form}
        return render(request, 'register.html', contexto)

def list_products(request):
    products = ProductModel.objects.all()
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
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Se salvar no Django ORM:
            #   form.save()
            #   return HttpResponseRedirect(reverse('list_products'))
            # else:
            #   form = ProductForm()

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
    return render(request, 'add_product.html', {'form': form})
