from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        strip=True,
        widget=forms.TextInput(attrs={"placeholder": "Search books..."})
    )

    def clean_query(self):
        q = self.cleaned_data.get("query", "")
        
        return q
