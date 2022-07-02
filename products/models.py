from distutils.command.upload import upload
from pydoc import describe
from unicodedata import category
from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=45)

class Categories(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

class Drink(models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)

class Images(models.Model):
    image = models.CharField(max_length=45)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

class Allergy(models.Model):
    name = models.CharField(max_length=45)

class AllergyDrink(models.Model):
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)

class Nutritions(models.Model):
    one_serving = models.DecimalField(max_digits = 10, decimal_places = 2)
    sodium = models.DecimalField(max_digits = 10, decimal_places = 2)
    saturated_fat = models.DecimalField(max_digits = 10, decimal_places = 2)
    sugars = models.DecimalField(max_digits = 10, decimal_places = 2)
    protein = models.DecimalField(max_digits = 10, decimal_places = 2)
    caffeine = models.DecimalField(max_digits = 10, decimal_places = 2)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    size = models.ForeignKey('Sizes', on_delete=models.CASCADE)

class Sizes(models.Model):
    name = models.CharField(max_length = 45)
    size_ml = models.CharField(max_length = 45)
    size_fluid = models.CharField(max_length = 45)
