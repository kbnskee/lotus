from django import forms


class PaginatedSearchForm(forms.Form):
    keyword=forms.CharField(max_length=90,required=False)
    per_page=forms.TypedChoiceField(coerce=int,choices=[(10, 10), (20, 20), (50, 50), (100,100)]) 

    keyword.widget.attrs.update({"class": "form-control form-control-sm"})
    per_page.widget.attrs.update({"class": "form-select form-select-sm"})