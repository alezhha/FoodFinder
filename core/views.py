from django.shortcuts import render
from .models import Dish, DishType, Product, ProductsType 

# Create your views here.
def base(request):
    return render(request, "dishes.html", {"Dishes":Dish.objects.all(), 
                                         "DishTypes":DishType.objects.all(), 
                                         "Products":Product.objects.all(), 
                                         "ProductTypes":ProductsType.objects.all()})
