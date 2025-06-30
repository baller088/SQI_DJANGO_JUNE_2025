from django.shortcuts import render

# Create your views here.

def available_dishes(request):
    return render(request, 'menu/dishes.html')
