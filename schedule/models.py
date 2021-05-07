from django.db import models
from django.contrib.auth.models import User

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE)
    date = models.DateTimeField()
