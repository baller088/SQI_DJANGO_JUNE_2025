from django.urls import path
from . import views

urlpatterns = [
    path('', views.practice_dtl, name='dtl_app')
]