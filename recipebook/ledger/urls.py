# <appname>/urls.py
from django.urls import path
from .views import index
from .views import recipe1, recipe2, recipes_list

urlpatterns = [
path('', index, name='index'),
path('recipes/list', recipes_list, name='recipes_list'),
path('recipe/1', recipe1, name='recipes_list'),
path('recipe/2', recipe2, name='recipes_list'),
]

app_name = "ledger"