from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}' (self.name)
    
    def ger_url(self):
        return reverse('ledger:recipe', args=[str(self.name)])

class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}' (self.name)
    
    def ger_url(self):
        return reverse('ledger:recipe', args=[str(self.name)])
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name = 'recipe'
    )
        
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name = 'ingredient'
    )