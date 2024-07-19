from django.contrib import admin
from .models import Product,Cart
# Register your models here.
admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields=('id',)
admin.site.register(Cart,ProductAdmin)


