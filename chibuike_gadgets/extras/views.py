from django.shortcuts import render, HttpResponse

# Create your views here.

def extras(request):
    return HttpResponse("<div>It is a big company that deals with selling of gadgets</div>")