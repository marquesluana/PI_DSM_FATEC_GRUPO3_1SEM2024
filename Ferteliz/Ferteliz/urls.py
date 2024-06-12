"""
URL configuration for Ferteliz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cadastroCliente/', views.cadastroCliente, name='cadastroCliente'),
    path('login/', views.login, name='login'),
    path('cadastroMenu', views.cadastroMenu, name='cadastroMenu'),
    path('cadastroVendedor', views.cadastroVendedor, name='cadastroVendedor'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('cadastroProdutos', views.cadastroProdutos, name='cadastroProdutos'),
    path('homeCliente', views.homeCliente, name='homeCliente'),
    path('homeVendedor', views.homeVendedor, name='homeVendedor'),    
    path('profileVendedor', views.profileVendedor, name='profileVendedor'), 
    path('profileCliente', views.profileCliente, name='profileCliente'), 
    path('add_product', views.add_product, name='add_product'), 
    path('list_products', views.list_products, name='list_products'),
]