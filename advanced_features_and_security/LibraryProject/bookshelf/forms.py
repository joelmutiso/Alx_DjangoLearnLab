from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    author = forms.CharField(max_length=100, required=True)
    published_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
