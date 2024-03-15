from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe
from django.contrib.auth.decorators import login_required



class RecipeList(ListView):
    model = Recipe 
    template_name = 'recipes_list.html'


@login_required
class Recipe(DetailView):
    model = Recipe
    template_name = 'recipe.html' 