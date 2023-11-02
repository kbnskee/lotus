from django.shortcuts import render

import pandas as pd

import openpyxl

from lotus.utils.PageFactory import (
    create_page_list as cpl,
    this_func_to_path as tftp
)

from lotus.forms import AppForm, ExcelImportForm

app_name = "Lotus Admin"
lotus_app='app'
lotus_page='page'
lotus_group='group'



######### START APP #########
def lotus_app_list(request):
    c=cpl(request,operation='-c',app_name=app_name)
    if request.method=="POST":
        return False
    elif request.method=="GET":
        form=AppForm()
    c['form']=form
    c['list']={}
    return render(request,tftp(subdir=lotus_app),c) 


def lotus_app_add(request):
    c=cpl(request,app_name=app_name)
    if request.method=="POST":
        return False
    elif request.method=="GET":
        form=AppForm()
    c['form']=form
    return render(request,tftp(subdir=lotus_app),c) 


def lotus_app_details(request,id):
    c=cpl(request,app_name=app_name)
    details=AppForm.objects.get(id=id)
    c['details']=details
    return render(request,tftp(subdir=lotus_app),c) 


def lotus_app_update(request):
    c=cpl(request,app_name=app_name)
    return render(request,tftp(subdir=lotus_app),c) 


def lotus_app_delete(request):
    c=cpl(request,app_name=app_name)
    return render(request,tftp(subdir=lotus_app),c) 
######### END APP #########


######### START PAGE #########
def lotus_page_add(request):
    c=cpl(request,app_name="Lotus Admin",page_name="Page")
    return render(request,tftp(subdir=lotus_page),c) 


def lotus_page_list(request):
    c=cpl(request,app_name="Lotus Admin",page_name="Page")
    return render(request,tftp(subdir=lotus_page),c) 


def lotus_page_details(request):
    c=cpl(request,app_name="Lotus Admin",page_name="Page")
    return render(request,tftp(subdir=lotus_page),c) 

def lotus_page_update(request):
    c=cpl(request,app_name="Lotus Admin",page_name="Page")
    return render(request,tftp(subdir=lotus_page),c) 


def lotus_page_delete(request):
    c=cpl(request,app_name="Lotus Admin",page_name="Page")
    return render(request,tftp(subdir=lotus_page),c) 
######### END PAGE #########


na_values = ['NA', 'na', 'N/A', 'n/a', '', 'NULL', 'null','nan']

def lotus_importer(request):
    from apps.conductms.models import ConductType,ConductCriteria
    c=cpl(request,app_name="Lotus Admin",page_name="Lotus Importer Page")
    if request.method=="POST":
        form=ExcelImportForm(request.POST,request.FILES)
        if form.is_valid():
            model=form.cleaned_data['model']
            excel_file=request.FILES['file']
            data=pd.read_excel(excel_file,engine='openpyxl',sheet_name=model)
            for index, row in data.iterrows():
                instance=eval(model + "()")
                for field in data.columns:
                    setattr(instance,field,row[field])
                instance.save()    
        else:
            print(form.errors)
    elif request.method=="GET":
        c['excel_importer_form']=ExcelImportForm()
    return render(request,tftp(subdir="importer"),c) 