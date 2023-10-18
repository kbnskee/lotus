from django import forms
from lotus.models import User,App,Page


class PaginatedSearchForm(forms.Form):
    keyword=forms.CharField(max_length=90,required=False)
    per_page=forms.TypedChoiceField(coerce=int,choices=[(10, 10), (20, 20), (50, 50), (100,100)]) 

    keyword.widget.attrs.update({"class": "form-control form-control-sm"})
    per_page.widget.attrs.update({"class": "form-select form-select-sm"})



class AppForm(forms.ModelForm):
    class Meta:
        model=App
        fields=['name','description','is_enabled','created_by']

        widgets={}
        widgets['name']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['description']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })


        