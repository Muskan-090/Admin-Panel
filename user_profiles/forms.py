from django import forms
from .models import UserProfile

class NewUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'designation','company','about', 'areas_of_interest']



class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Search...'}))

       