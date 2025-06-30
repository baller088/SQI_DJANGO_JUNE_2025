from django.shortcuts import render , get_object_or_404, HttpResponse,redirect

from .models import Artist, Album
from .form import ArtistCreateForm
from .form import ArtistCreateNotModelForm

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def artists(request):
    context = {
        'artists': Artist.objects.order_by('debut_year'),
    }
    return render(request, "core/artists.html", context)


def albums(request):
    context = {
        'albums': Album.objects.order_by('release_date'),
    }
    return render(request, "core/albums.html", context)

def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    context = {"artist": artist}
    return render(request, "core/artist_detail.html", context)
def album_detail(request, album_pk):
    album = get_object_or_404(Album, pk=album_pk)
    context = {"album": album}
    return render(request, "core/album_detail.html", context)

def create_artist(request):
    form = ArtistCreateForm()
    if request.method == "POST":
        form = ArtistCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('core:artists')
    context = {
        'create_artist_form' : form
    }
    return render(request, "core/create_artist.html", context)

def create_album(request):
    create_album_form = ArtistCreateNotModelForm
    if request.method == "POST":
        create_album_form = ArtistCreateNotModelForm(request.POST, request.FILES)
        if create_album_form.is_valid():
            cleaned_data = create_album_form.cleaned_data
            Album.objects.create(
                name = cleaned_data.get('name'),
                debut_year = cleaned_data.get('debut_year'),
                image = cleaned_data.get('image')
            )
            return redirect('core:albums')
        
    context = {
        'form': create_album_form
    }

    return render(request, "core/create_album.html", context)



