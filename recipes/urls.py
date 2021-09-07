
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='yumbo-home'),
    # path('about/', views.about, name='yumbo-about'),
    # path('recipes/', views.recipes, name='recipes'),
    path('recipes/<int:recipe_id>', views.recipe_detail, name='recipe-detail'),
    path('create-recipe/', views.create_recipe, name='create-recipe'),
    path('edit-recipe/<int:recipe_id>', views.edit_recipe, name='edit-recipe'),
    path('delete-recipe/<int:recipe_id>', views.delete_recipe, name='delete-recipe'),
]
