from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    telefone = models.TextField(max_length=11, blank=True)
    cpf = models.CharField('CPF', max_length=30, default='')

    def __str__(self):
        return self.nome

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name