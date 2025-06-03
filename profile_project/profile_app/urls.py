from django.urls import path

from . import views

urlpatterns = [
    path('', views.goals, name='goals'),
    path('', views.hobbies, name='hobbies'),
    path('', views.index, name='index'),
]