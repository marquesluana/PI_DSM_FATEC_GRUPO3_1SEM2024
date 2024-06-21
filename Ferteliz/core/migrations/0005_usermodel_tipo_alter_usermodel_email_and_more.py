# Generated by Django 4.1.13 on 2024-06-15 03:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_endereço_usermodel_endereco_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='tipo',
            field=models.CharField(default='cliente', max_length=8),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator(message='Por favor, insira um endereço de email válido.')]),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='telefone',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]