from django import forms
from django.core.exceptions import ValidationError

from .services.connection import get_db
from .models import ProductModel, UserModel, VendaModel
import re

def validate_cpf(value):
    if len(value) != 11 or not value.isdigit():
        raise ValidationError('CPF precisa ter 11 dígitos numéricos.')

class VendaForm(forms.ModelForm):
    class Meta:
        model = VendaModel
        fields = ['dataVenda', 'codigoVenda', 'codigoCliente', 'codigoFornecedor', 'name', 'description', 'quantidade', 'valorUnitario', 'valorTotal']
        widgets = {
            'dataVenda': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data da Venda'}),
            'codigoVenda': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código da Venda'}),
            'codigoCliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código do Cliente'}),
            'codigoFornecedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código do Fornecedor'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do produto'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade'}),
            'valorUnitario': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor Unitário'}),
            'valorTotal': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor Total'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['name', 'description', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do produto'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor'}),
        }
        
    
    def save(self, commit=True):
        # Acessar os dados do formulário após a validação
        cleaned_data = self.cleaned_data
        name = cleaned_data.get('name', '')
        description = cleaned_data.get('description', '')
        price = cleaned_data.get('price', 0)

        # Imprimir os dados no console
        print(f'Name: {name}, Description: {description}, Price: {price}')

        # Inserir dados no MongoDB
        product = get_db().products.insert_one({
            'name': name,
            'description': description,
            'price': float(price)
        })      
        return product


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}),
        max_length=128
    )

    class Meta:
        model = UserModel
        fields = ['username', 'cpf', 'telefone', 'cep', 'endereço', 'numero', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP'}),
            'endereço': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço'}),
            'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número'}),
        }

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper().strip()

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if re.match(r'^\(\d{2}\) \d{4,5}-\d{4}$', telefone):
            return telefone
        raise ValidationError('Telefone precisa ter 10 ou 11 caracteres (Ex: 19 99999 9999)')

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        validate_cpf(cpf)
        return cpf
    
    def clean_rua(self):
        rua = self.cleaned_data['rua']
        return rua.upper()
    
    def clean_bairro(self):
        bairro = self.cleaned_data['bairro']
        if bairro:
            return bairro.upper().strip()
        else:
            raise ValidationError('Campo vazio e/ou inválido.')

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
