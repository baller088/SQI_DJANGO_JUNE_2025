from django.shortcuts import render, HttpResponse

# Create your views here.

def gadgets(request):
    return HttpResponse("""
    <ol>
        <li>Phones</li>
        <li>Laptops</li>
        <li>WristWatch</li>
        <li>Television</li>
    </ol>
""")
