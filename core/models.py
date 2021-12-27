from django.db import models

# Create your models here.

class ProductsType(models.Model):
    productTypeName = models.CharField("Название категории продукта", max_length=255)

    def __str__(self):
        return self.productTypeName

class Product(models.Model):
    productName = models.CharField("Название продукта", max_length=255)
    productType = models.ForeignKey("ProductsType", on_delete=models.CASCADE)

    def __str__(self):
        return self.productName



class DishType(models.Model):
    dishTypeName = models.CharField("Название категории блюда", max_length=255)

    def __str__(self):
        return self.dishTypeName

class Dish(models.Model):
    dishName = models.CharField("Название блюда", max_length=255, default="0")
    diff = {
        ("Easy", "Легко"),
        ("Medium", "Средне"),
        ("Hard", "Сложно"),
    }
    difficulty = models.CharField("Сложность", max_length=10, choices=diff, default="Легко")
    products = models.ManyToManyField(Product)
    dishTtype = models.ForeignKey(DishType, on_delete=models.CASCADE, default="0")
    photo = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.dishName