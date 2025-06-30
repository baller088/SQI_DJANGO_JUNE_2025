from django import forms
from . models import Artist

class ArtistCreateForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = "__all__"


class ArtistCreateNotModelForm(forms.Form):
    name = forms.CharField(max_length=255)
    debut_year = forms.IntegerField()
    image = forms.ImageField()
