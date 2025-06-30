from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import Recipe

# Create your views here.

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe:list_recipe')
    else:
        form =RecipeForm()
    return render(request, 'recipe/add_recipe.html', {'form':form})

def list_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/list_recipe.html', {'recipes':recipes})

