from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(min_length=255)

    def __str__(self):
        return '{}'.format(self.name)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[self.pk])


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        Profile,
        null=True,
        default=None,
        on_delete=models.CASCADE,
        related_name="users"
    )
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[self.pk])
    

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
        related_name = 'ingredients'
    )