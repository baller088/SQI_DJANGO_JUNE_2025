from django.urls import path
from .import views

app_name = 'book_review'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('update_review/<int:review_pk>/', views.update_review, name='update_review'),
    path('confirm_delete/<int:review_pk>/', views.confirm_delete, name='confirm_delete'), 
    path('delete_book/<int:review_pk>/', views.delete_book, name='delete_book'),
]
