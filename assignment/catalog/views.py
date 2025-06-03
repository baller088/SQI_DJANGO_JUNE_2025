from django.shortcuts import render, HttpResponse

# Create your views here.

def booktitles(request):
    return HttpResponse("The Saint, Lekki Headmaster")