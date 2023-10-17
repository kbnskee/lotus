from django import forms


class KeywordSearchForm(forms.Form):
    keyword = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class':'form-control form-control-sm',
                'placeholder':"Enter Search keyword",
                'required':False
            }
        )
    )