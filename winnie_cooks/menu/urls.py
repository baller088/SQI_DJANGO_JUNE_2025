from django.urls import path
from . import views

app_name = 'menu'
urlpatterns = [
    path('available_dishes/', views.available_dishes, name='available_dishes'),
]