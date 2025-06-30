from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('add/', views.add_recipe, name='add_recipe'),
    path('', views.list_recipes, name='list_recipe'),
]