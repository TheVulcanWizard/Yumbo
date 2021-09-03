from django import forms
from .models import Recipe, Ingredient, Direction

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'prep_time', 'image']
        widgets = {
            'recipe_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recipe Name'}),
            'prep_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prep Time'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['position', 'ingredient_name', 'quantity', 'units']
        widgets = {
            'position': forms.HiddenInput(),
            'ingredient_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingredient Name'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'units': forms.Select(attrs={'class': 'form-select'}),
        }

class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = ['position', 'header', 'text']
        widgets = {
            'position': forms.HiddenInput(),
        }
