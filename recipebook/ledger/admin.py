from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Recipe, RecipeIngredient, Ingredient, Profile




class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInLine,]


class RecipeInline(admin.StackedInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeInline]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)