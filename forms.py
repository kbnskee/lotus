from django import forms
from lotus.models import App, Page, Group, GroupApp, GroupPage, UserGroup


class PaginatedSearchForm(forms.Form):
    keyword=forms.CharField(max_length=90,required=False)
    per_page=forms.TypedChoiceField(coerce=int,choices=[(10, 10), (20, 20), (50, 50), (100,100)]) 

    keyword.widget.attrs.update({"class": "form-control form-control-sm"})
    per_page.widget.attrs.update({"class": "form-select form-select-sm"})



class AppForm(forms.ModelForm):
    class Meta:
        model=App
        fields=['id','name','description','is_enabled','created_by']

        widgets={}
        widgets['id']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['name']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['description']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['is_enabled']=forms.Select(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        },choices=[(True, 'Enabled'), (False, 'Disabled')])


class AppUpdateForm(forms.ModelForm):
    class Meta:
        model=App
        fields=['id','name','description','is_enabled','updated_by']

        widgets={}
        widgets['id']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['name']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['description']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['is_enabled']=forms.Select(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        },choices=[(True, 'Enabled'), (False, 'Disabled')])


class PageForm(forms.ModelForm):
    class Meta:
        model=Page
        fields=['id','app','name','description','path','is_enabled','created_by']

        widgets={}
        widgets['app']=forms.Select(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['id']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['name']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['description']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['path']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['is_enabled']=forms.Select(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        },choices=[(True, 'Enabled'), (False, 'Disabled')])


class PageUpdateForm(forms.ModelForm):
    class Meta:
        model=Page
        fields=['id','app','name','description','path','is_enabled','updated_by']

        widgets={}
        widgets['app']=forms.Select(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['id']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['name']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['description']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['path']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['is_enabled']=forms.Select(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        },choices=[(True, 'Enabled'), (False, 'Disabled')])


class GroupForm(forms.ModelForm):
    class Meta:
        model=Group
        fields=['id','name','description','is_enabled','created_by']

        widgets={}

        widgets['id']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['name']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['description']=forms.TextInput(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        widgets['is_enabled']=forms.Select(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        },choices=[(True, 'Enabled'), (False, 'Disabled')])


class GroupAppForm(forms.ModelForm):
    
    class Meta:
        model=GroupApp
        fields=['app']

        widgets={}

        widgets['app']=forms.Select(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
    def __init__(self, *args, **kwargs):
        app_list = kwargs.pop('apps')
        super(GroupAppForm, self).__init__(*args, **kwargs)
        self.fields['app'].queryset = App.objects.exclude(id__in=app_list)
    


class GroupPageForm(forms.ModelForm):
    class Meta:
        model=GroupPage
        fields=['page']
    def __init__(self, *args, **kwargs):
        app_list = kwargs.pop('apps')
        page_list = kwargs.pop('pages')
        super(GroupPageForm, self).__init__(*args, **kwargs)
        print(f"app list: {app_list}")
        print(f"page list: {page_list}")

        app_pages=Page.objects.filter(app__in=app_list)
        pages=app_pages.exclude(id__in=page_list)
        self.fields['page'].queryset = pages
        


class UserGroupForm(forms.ModelForm):
    class Meta:
        model=UserGroup
        fields=['group']

        widgets={}
        widgets['group']=forms.Select(attrs={
            'class':'form-control form-control-sm border-1 border-dark',
            'style':'background-color:#636363; color:#ccc;'
        })
        


class UserGroupAddForm(forms.ModelForm):
    class Meta:
        model=UserGroup
        fields=['group','user']

        widgets={}
        widgets['group']=forms.Select(attrs={
            'class':'form-control form-control-sm',
        })
        widgets['user']=forms.Select(attrs={
            'class':'form-control form-control-sm',
        })


class ModelUploadForm(forms.Form):
    file = forms.FileField()      


class ImportExcelForm(forms.Form):
    file = forms.FileField()


class ExcelImportForm(forms.Form):
    file = forms.FileField(label='Select an Excel file')
    model=forms.CharField(max_length=90,required=False)
        