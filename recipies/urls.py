from django.urls import path

from .views import RecipeList, create_recipe, DeleteAllRecipes, RecipeDetail

urlpatterns = [
    path('recipies/', RecipeList.as_view()),
    path('create/', create_recipe, name='create_recipe'),
    path('recipes/delete/', DeleteAllRecipes.as_view(), name='delete-all-recipes'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
]