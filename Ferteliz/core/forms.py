from django import forms
from django.core.exceptions import ValidationError
from .models import ProductModel, UserModel, VendaModel

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
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do produto'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

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
