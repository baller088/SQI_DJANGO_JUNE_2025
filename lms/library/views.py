from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "library/home.html")

def book_list(request):
    return render(request, "library/list-of-books.html")