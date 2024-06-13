from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel, ProductModel, VendaModel

admin.site.register(UserModel, UserAdmin)
admin.site.register(ProductModel)
admin.site.register(VendaModel)