from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel
from .models import ProductModel

admin.site.register(UserModel, UserAdmin)
admin.site.register(ProductModel)