from django.shortcuts import render, HttpResponse

# Create your views here.

def events(request):
    return HttpResponse("<section> A new book release</section>")