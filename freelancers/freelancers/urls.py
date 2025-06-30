from django.urls import path
from . import views

app_name = 'freelancers'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('case_studies/', views.case_studies, name='case_studies'),
    path('pricing/', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
    path('testimonials/', views.testimonials, name='testimonials'),
]