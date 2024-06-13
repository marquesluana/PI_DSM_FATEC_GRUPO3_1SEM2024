from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastroCliente', views.cadastroCliente, name='cadastroCliente'),
    path('list_products', views.list_products, name='list_products'),
    path('cadastroVendedor', views.cadastroVendedor, name='cadastroVendedor'),
    path('cadastroProdutos', views.cadastroProdutos, name='cadastroProdutos'),
    path('carrinho', views.carrinho, name='carrinho'),
    path('login', views.login, name='login'),
    path('profileCliente', views.profileCliente, name='profileCliente'),
    path('profileVendedor', views.profileVendedor, name='profileVendedor'),
]
