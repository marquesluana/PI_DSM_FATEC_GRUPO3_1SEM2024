from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import ProductModel, UserModel

def validate_cpf(value):
    if len(value) != 11 or not value.isdigit():
        raise ValidationError('CPF precisa ter 11 dígitos numéricos.')

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do produto'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}),
        max_length=128
    )

    class Meta:
        model = UserModel
        fields = ['username', 'cpf', 'telefone', 'rua', 'bairro', 'numero', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'rua': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rua'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
            'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número'}),
        }

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if len(telefone) <= 11:
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
        return bairro.upper()

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
