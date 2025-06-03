from django.urls import path
from . import views
urlpatterns=[
    path("about/us/", views.extras, name="extra")
]