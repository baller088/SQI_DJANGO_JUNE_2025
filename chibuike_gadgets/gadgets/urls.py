from django.urls import path
from . import views
urlpatterns=[
    path('gadgets/',views.gadgets, name='gadgets' )
]