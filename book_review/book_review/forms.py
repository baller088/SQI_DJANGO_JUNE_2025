from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer_name', 'rating', 'comment']

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if not (1 <= rating <= 5):
            raise forms.ValidationError("Rating must be between 1 and 5")
        return rating