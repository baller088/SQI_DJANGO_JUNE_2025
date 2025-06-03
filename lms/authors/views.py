from django.shortcuts import render

# Create your views here.
from django.http import render

def all_authors(request):
    return render(request, "authors/html" )

def book_signings(request):
    return render(request, "authors/book-signongs.html")