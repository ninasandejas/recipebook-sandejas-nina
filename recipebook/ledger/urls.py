# <appname>/urls.py
from django.urls import path
from .views import RecipeList, Recipe


urlpatterns = [
    path('recipes/list', RecipeList.as_view(), name='recipe_site'),
    path('recipe/<int:pk>/', Recipe.as_view(), name='recipe'),
]

app_name = "ledger"