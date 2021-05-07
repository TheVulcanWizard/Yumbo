from django.forms import ModelForm
from django.apps import apps
from .models import Meal

Recipe = apps.get_model('recipes', 'Recipe')

class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = ['meal_recipe']

    def __init__(self, user, *args, **kwargs):
        super(MealForm, self).__init__(*args, **kwargs)
        self.fields['meal_recipe'].queryset = Recipe.objects.filter(user=user)