from django.urls import path

from .views import RecipeList, create_recipe

urlpatterns = [
    path('recipies/', RecipeList.as_view()),
    path('create/', create_recipe, name='create_recipe'),
]