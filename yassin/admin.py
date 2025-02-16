from django.contrib import admin
from .models import Product,Identity

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name','price')
    
class IdentityAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','age')
    
    
admin.site.register(Product)
admin.site.register(Identity, IdentityAdmin)

# Register your models here.
