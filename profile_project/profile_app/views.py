from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'profile_app/index.html')
def hobbies(request):
    return render(request, 'profile_app/hobbies.html')
def goals(request):
    return render(request, 'profile_app/goals.html')