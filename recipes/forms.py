from django import forms
from .models import Recipe, Ingredient, Direction

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'prep_time', 'image']
        widgets = {
            'recipe_name': forms.TextInput(attrs={'class': 'form-control friendly-input', 'placeholder': 'Recipe Name'}),
            'prep_time': forms.TextInput(attrs={'class': 'form-control friendly-input', 'placeholder': 'Prep Time'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['position', 'ingredient_name', 'quantity', 'units']
        widgets = {
            'position': forms.HiddenInput(),
            'ingredient_name': forms.TextInput(attrs={'class': 'form-control friendly-input', 'placeholder': 'Ingredient Name'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control friendly-input'}),
            'units': forms.Select(attrs={'class': 'form-select friendly-input'}),
        }

class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = ['position', 'header', 'text']
        widgets = {
            'position': forms.HiddenInput(),
            'header': forms.TextInput(attrs={'class': 'form-control friendly-input'}),
            'text': forms.Textarea(attrs={'class': 'form-control friendly-input', 'rows': 4})
        }
