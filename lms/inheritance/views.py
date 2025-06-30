from django.shortcuts import render

# Create your views here.

def demo_inheritance(request):
    return render(request, 'demo_inheritance/inheritance.html',)