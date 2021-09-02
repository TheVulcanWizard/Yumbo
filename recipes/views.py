
#TODO: Turn base directory into a landing page if not logged in, but a user home page if they are logged in? See how this might affect performance.

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from .models import Recipe, Ingredient, Direction
from .forms import RecipeForm, IngredientForm, DirectionForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404

@login_required
def home(request):
    context = {
        'recipes': Recipe.objects.filter(user=request.user),
    }
    return render(request, 'recipes/home.html', context)

def about(request):
    return render(request, 'recipes/about.html')

@login_required
def recipes(request):
    #creating this view in the event that our home dashboard differs from a recipe focused view
    context = {
        'recipes': Recipe.objects.filter(user=request.user),
    }
    return render(request, 'recipes/home.html', context)

@login_required
def recipe_detail(request, recipe_id):
    context = {
        'recipe': Recipe.objects.get(user=request.user, pk=recipe_id),
        'ingredients': Ingredient.objects.filter(recipe=recipe_id),
        'directions': Direction.objects.filter(recipe=recipe_id).order_by('position'),
    }
    if context['recipe']:
        return render(request, 'recipes/recipe_detail.html', context)
    else:
        raise Http404('You shouldn\'t be here...')

@login_required
def create_recipe(request):
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES)
        ingredient_formset = inlineformset_factory(Recipe, Ingredient, form=IngredientForm, can_delete=True)
        ingredient_forms = ingredient_formset(request.POST)
        direction_formset = inlineformset_factory(Recipe, Direction, form=DirectionForm, can_delete=True)
        direction_forms = direction_formset(request.POST)
        print("POST")
        if recipe_form.is_valid() and ingredient_forms.is_valid() and direction_forms.is_valid():
            recipe = recipe_form.save(False)
            recipe.user = request.user
            recipe.save()

            ingredients = ingredient_forms.save(False)
            for ingredient in ingredients:
                ingredient.recipe = recipe
                ingredient.save()

            directions = direction_forms.save(False)
            for direction in directions:
                direction.recipe = recipe
                direction.save()

            return redirect('recipe-detail', recipe_id=recipe.pk)
    else:
        recipe_form = RecipeForm()
        ingredient_formset = inlineformset_factory(Recipe, Ingredient, form=IngredientForm, extra=1)
        ingredient_forms = ingredient_formset(initial=[{'position':0}])
        direction_formset = inlineformset_factory(Recipe, Direction, form=DirectionForm, extra=1)
        direction_forms = direction_formset(initial=[{'position':0}])

    context = {
        'recipe_form': recipe_form,
        'ingredient_forms': ingredient_forms,
        'direction_forms': direction_forms,
    }

    return render(request, 'recipes/recipe_form.html', context)

@login_required
def edit_recipe(request, recipe_id):
    recipe_instance = get_object_or_404(Recipe, pk=recipe_id)
    ingredient_formset = inlineformset_factory(Recipe, Ingredient, form=IngredientForm, extra=0, can_delete=True)
    direction_formset = inlineformset_factory(Recipe, Direction, form=DirectionForm, extra=0, can_delete=True)

    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES, instance=recipe_instance)
        ingredient_forms = ingredient_formset(request.POST, instance=recipe_instance)
        direction_forms = direction_formset(request.POST, instance=recipe_instance)

        if recipe_form.is_valid() and ingredient_forms.is_valid() and direction_forms.is_valid():
            recipe = recipe_form.save()

            ingredients = ingredient_forms.save(False)
            for ingredient in ingredient_forms.deleted_objects:
                ingredient.delete()
            for ingredient in ingredients:
                ingredient.recipe = recipe
                ingredient.save()

            directions = direction_forms.save(False)
            for direction in direction_forms.deleted_objects:
                direction.delete()
            for direction in directions:
                direction.recipe = recipe
                direction.save()

            return redirect('recipe-detail', recipe_id=recipe.pk)
    else:
        recipe_form = RecipeForm(instance=recipe_instance)
        ingredient_formset = inlineformset_factory(Recipe, Ingredient, form=IngredientForm, extra=0)
        ingredient_forms = ingredient_formset(instance = recipe_instance)
        direction_formset = inlineformset_factory(Recipe, Direction, form=DirectionForm, extra=0)
        direction_forms = direction_formset(instance=recipe_instance)

    context = {
        'recipe': Recipe.objects.get(user=request.user, pk=recipe_id),
        'recipe_form': recipe_form,
        'ingredient_forms': ingredient_forms,
        'direction_forms': direction_forms,
    }

    return render(request, 'recipes/recipe_form.html', context)

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        recipe.delete()
        return redirect('/')

    context = {
        'recipe': recipe
    }

    return render(request, 'recipes/delete_recipe.html', context)