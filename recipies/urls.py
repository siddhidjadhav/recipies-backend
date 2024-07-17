from django.urls import path

from .views import RecipeList

urlpatterns = [
    path('recipies/', RecipeList.as_view()),
]