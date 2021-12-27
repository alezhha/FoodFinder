from django.contrib import admin

from core.models import DishType, ProductsType, Product, Dish

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("productName", "productType")

admin.site.register(Product, ProductAdmin)

class ProductsTypeAdmin(admin.ModelAdmin):
    list_display = ("productTypeName",)

admin.site.register(ProductsType, ProductsTypeAdmin)

class DishAdmin(admin.ModelAdmin):
    list_display = ("dishName", "difficulty", "dishTtype")

admin.site.register(Dish, DishAdmin)

class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("dishTypeName", )

admin.site.register(DishType, DishTypeAdmin)