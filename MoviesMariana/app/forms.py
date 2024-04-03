from django import forms

class GenreFilterForm(forms.Form):
    genre = forms.ChoiceField(choices=[('', 'All')] + [(genre, genre) for genre in ['Action', 'Comedy', 'Drama']], required=False)
