from django.shortcuts import render, HttpResponse

# Create your views here.

def books(request):
    return HttpResponse("""
<ol>
<ul>Storybooks</ul>
<ul>Textbooks</ul>
<ul>Novels</ul>
<ul>Notebooks</ul>
<ul>Joters</ul>
</ol>
""")
