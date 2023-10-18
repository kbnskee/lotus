from django.shortcuts import render

from lotus.utils.PageFactory import (
    create_page_list as cpl,
    this_func_to_path as tftp
)

from lotus.forms import AppForm

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