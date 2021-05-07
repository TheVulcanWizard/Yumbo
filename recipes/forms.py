from django.forms import ModelForm, HiddenInput
from .models import Recipe, Ingredient, Direction

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'prep_time', 'image']

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['position', 'ingredient_name', 'quantity', 'units']
        widgets = {
            'position': HiddenInput(),
        }

class DirectionForm(ModelForm):
    class Meta:
        model = Direction
        fields = ['position', 'text']
        widgets = {
            'position': HiddenInput(),
        }
