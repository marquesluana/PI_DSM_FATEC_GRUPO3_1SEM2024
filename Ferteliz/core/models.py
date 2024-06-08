from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    telefone = models.TextField(max_length=11, blank=True)
    cpf = models.CharField('CPF', max_length=30, default='')
    rua = models.CharField(max_length=20, blank=True)
    bairro = models.CharField(max_length=15)
    numero = models.CharField(max_length=5)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class ProductModel(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return self.name