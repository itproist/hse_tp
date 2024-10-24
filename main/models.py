from django.db import models

class Product(models.Model):
    name = models.TextField()
    measure_type = models.enums

class Dish(models.Model):
    name = models.TextField()
    time = models.DurationField()
    dish_cuisine = models.enums
    recipy = models.TextField()

class Ingredient(models.Model):
    dish = models.ForeignKey("Dish", on_delete=models.CASCADE, null=False)
    product = models.ForeignKey("Product", on_delete=models.CASCADE, null=False)
    amount = models.IntegerField()
