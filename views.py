from django.shortcuts import render,redirect

import pandas as pd

import openpyxl

from django.db.models import Q

from lotus.utils.PageFactory import (
    create_page_list as cpl,
    this_func_to_path as tftp
)

from lotus.models import App, Page, Group, GroupApp, GroupPage

from lotus.forms import (
    AppForm, AppUpdateForm,
    PageForm, PageUpdateForm, 
    GroupForm, GroupAppForm, GroupPageForm, 
    ExcelImportForm,
    )

app_name = "Lotus Admin"
lotus_app='app'
lotus_page='page'
lotus_group='group'


def nav_list():
    nav_list={
        "lotus_app_list": {
            "id":2,
            "state":"",
            "name":"Applications",
            "pathname":"lotus_app_list"
            },
        "lotus_page_list": {
            "id":2,
            "state":"",
            "name":"Pages",
            "pathname":"lotus_page_list"
            },
        "lotus_group_list": {
            "id":2,
            "state":"",
            "name":"Groups",
            "pathname":"lotus_group_list"
            },
        }
    return nav_list


######### START APP #########
def lotus_app_list(request):
    c=cpl(request,nav_list=nav_list(),operation='-c',app_name=app_name)
    c['form']=AppForm()
    c['list']=App.objects.all()
    return render(request,tftp(subdir=lotus_app),c) 


def lotus_app_add(request):
    if request.method=="POST":
        form=AppForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return redirect('lotus_app_list') 


def lotus_app_details(request,id):
    c=cpl(request,nav_list=nav_list(),app_name=app_name)
    details=App.objects.get(id=id)
    list=Page.objects.filter(app=details)
    c['details']=details
    c['list']=list    
    c['app_group_list']=GroupApp.objects.filter(app=details)
    return render(request,tftp(subdir=lotus_app),c) 



def lotus_app_update(request,id):
    c=cpl(request,nav_list=nav_list(),app_name=app_name)
    details=App.objects.get(id=id)
    list=Page.objects.filter(app=details)
    if request.method=="POST":
        form=PageUpdateForm(request.POST, instance=details)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.updated_by=request.user
            instance.save()
            return redirect('lotus_app_details',id)
        else:
            print(form.errors)
    else:
        c['form']=AppUpdateForm(instance=details)
    c['details']=details
    c['list']=list    
    c['app_group_list']=GroupApp.objects.filter(app=details)
    return render(request,tftp(subdir=lotus_app),c) 


def lotus_app_delete(request):
    c=cpl(request,nav_list=nav_list(),app_name=app_name)
    return render(request,tftp(subdir=lotus_app),c) 
######### END APP #########


######### START PAGE #########
def lotus_page_list(request):
    c=cpl(request,nav_list=nav_list(),operation='-c',app_name=app_name)
    c['form']=PageForm()
    c['list']=Page.objects.all()
    return render(request,tftp(subdir=lotus_page),c) 


def lotus_page_add(request):
    if request.method=="POST":
        form=PageForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return redirect('lotus_page_list') 


def lotus_page_details(request,id):
    c=cpl(request,nav_list=nav_list(),app_name="Lotus Admin",page_name="Page")
    details=Page.objects.get(id=id)
    
    c['details']=details
    return render(request,tftp(subdir=lotus_page),c) 

def lotus_page_update(request,id):
    c=cpl(request,nav_list=nav_list(),app_name="Lotus Admin",page_name="Page")
    details=Page.objects.get(id=id)
    if request.method=="POST":
        form=PageUpdateForm(request.POST,instance=details)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.updated_by=request.user
            instance.save()
            return redirect('lotus_page_details',id)
        else:
            print(form.errors)
    else:
        c['form']=PageUpdateForm(instance=details)
    c['details']=details
    return render(request,tftp(subdir=lotus_page),c) 


def lotus_page_delete(request):
    c=cpl(request,nav_list=nav_list(),app_name="Lotus Admin",page_name="Page")
    return render(request,tftp(subdir=lotus_page),c) 
######### END PAGE #########


######### START GROUPS #########
def lotus_group_list(request):
    c=cpl(request,nav_list=nav_list(),operation='-c',app_name=app_name)
    c['form']=GroupForm()
    c['list']=Group.objects.all()
    return render(request,tftp(subdir=lotus_group),c) 


def lotus_group_add(request):
    if request.method=="POST":
        form=GroupForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return redirect('lotus_group_list') 


def lotus_group_details(request,id):
    c=cpl(request,nav_list=nav_list(),app_name="Lotus Admin",page_name="Groups")
    details=Group.objects.get(id=id)
    group_app_list=GroupApp.objects.filter(group=details)
    app_list = [item['app'] for item in group_app_list.values('app')]
    page_list=Page.objects.filter(app__in=app_list)
    group_page_list=GroupPage.objects.filter(group=details)
    page_value_list=[item['id'] for item in page_list.values('id')]

    c['group_app_form']=GroupAppForm()
    c['group_page_form']=GroupPageForm(apps=app_list)
    
    c['group_app_list']=group_app_list
    c['group_page_list']=group_page_list
    c['details']=details
    
    return render(request,tftp(subdir=lotus_group),c) 


def lotus_group_app_add(request,group):
    if request.method=="POST":
        form=GroupAppForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.group_id=group
            instance.save()
        else:
            print(form.errors)
    return redirect('lotus_group_details',group) 


def lotus_group_page_add(request,group):
    group_app_list=GroupApp.objects.filter(group=group)
    app_list = [item['app'] for item in group_app_list.values('app')]
    if request.method=="POST":
        form=GroupPageForm(request.POST,apps=app_list)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.group_id=group
            instance.save()
        else:
            print(form.errors)
    return redirect('lotus_group_details',group) 

def lotus_group_app_delete(request,group,app):
    instance=GroupApp.objects.get(id=app)
    instance.delete()
    return redirect('lotus_group_details',group) 

def lotus_group_update(request):
    c=cpl(request,nav_list=nav_list(),app_name="Lotus Admin",page_name="Groups")
    return render(request,tftp(subdir=lotus_group),c) 



def lotus_group_delete(request):
    c=cpl(request,nav_list=nav_list(),app_name="Lotus Admin",page_name="Groups")
    return render(request,tftp(subdir=lotus_group),c) 
######### END GROUPS #########

######### START USER GROUPS #########
######### END USER GROUPS #########




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



def lotus_404(request,violation,message):
    c=cpl(request,app_name="Lotus",page_name="Access Violation")

    return render(request,tftp(subdir="warning"),c) 