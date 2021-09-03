from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from random import choice
from os.path import join, isfile
from os import listdir

def random_img():
    dir_path = 'media/recipe_pics/defaults'
    files = [content for content in listdir(dir_path) if isfile(join(dir_path, content))]
    return join('recipe_pics/defaults', choice(files))

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name = models.CharField("Recipe Name", max_length=200)
    prep_time = models.CharField("Prep Time", max_length=30)
    image = models.ImageField(default=random_img, upload_to='recipe_pics')

    def __str__(self):
        return self.recipe_name
    
class Ingredient(models.Model):
    UNIT_CHOICES = [('tsp', 'teaspoon'), ('tbsp', 'tablespoon'), ('lb', 'pound'), ('g', 'gram'), ('cup', 'cup'), ('oz', 'fluid ounce'), ('gal', 'gallon'), ('quart', 'quart'), ('pint', 'pint'), ('mL', 'milliliter'), ('L', 'liter'), ('dash', 'dash'), ('pinch', 'pinch'), ('stick', 'stick'),]

    ingredient_name = models.CharField("Ingredient Name", max_length=100)
    position = models.IntegerField(blank=False)
    quantity = models.DecimalField("Quantity", max_digits=10, decimal_places=5, null=True)
    units = models.CharField(max_length=5, choices=UNIT_CHOICES, blank=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient_name + ', ' + self.recipe.recipe_name

class Direction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    position = models.IntegerField(blank=False)
    header = models.CharField("Direction Header", max_length=140)
    text = models.TextField("Instructions", blank=True)

    def __str__(self):
        return str(self.position) + ', ' + self.recipe.recipe_name
        