from django.shortcuts import render,redirect

#import pandas as pd


from django.db.models import Q

from lotus.utils.PageFactory import (
    create_page_list as cpl,
    this_func_to_path as tftp
)

from lotus.models import User, UserGroup, App, Page, Group, GroupApp, GroupPage

from lotus.forms import (
    AppForm, AppUpdateForm,
    PageForm, PageUpdateForm, 
    GroupForm, GroupAppForm, GroupPageForm, 
    ExcelImportForm,
    UserGroupForm, UserGroupAddForm,
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
        "lotus_user_list": {
            "id":2,
            "state":"",
            "name":"System Users",
            "pathname":"lotus_user_list"
            }
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
    page_id_list=[item['page'] for item in group_page_list.values('page')]

    c['group_app_form']=GroupAppForm(apps=app_list)
    c['group_page_form']=GroupPageForm(apps=app_list,pages=page_id_list)
    
    c['group_app_list']=group_app_list
    c['group_page_list']=group_page_list
    c['details']=details
    
    return render(request,tftp(subdir=lotus_group),c) 


def lotus_group_app_add(request,group):
    details=Group.objects.get(id=group)
    group_app_list=GroupApp.objects.filter(group=details)
    app_list = [item['app'] for item in group_app_list.values('app')]
    if request.method=="POST":
        form=GroupAppForm(request.POST,apps=app_list)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.group_id=group
            instance.save()
        else:
            print(form.errors)
    return redirect('lotus_group_details',group) 


def lotus_group_page_add(request,group):
    group_app_list=GroupApp.objects.filter(group=group)
    details=Group.objects.get(id=group)
    group_app_list=GroupApp.objects.filter(group=details)
    app_list = [item['app'] for item in group_app_list.values('app')]
    
    group_page_list=GroupPage.objects.filter(group=details)
    page_value_list=[item['id'] for item in group_page_list.values('id')]
    
    if request.method=="POST":
        form=GroupPageForm(request.POST,apps=app_list,pages=page_value_list)
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
def lotus_user_list(request):
    c=cpl(request,nav_list=nav_list(),app_name=app_name)
    employee_list=User.objects.prefetch_related('usergroup_set','employee').all()
    c['employee_list']=employee_list
    student_list=User.objects.prefetch_related('usergroup_set','student').all()
    c['student_list']=student_list
    return render(request,tftp(subdir="user"),c) 


def lotus_user_employee_details(request,id):
    c=cpl(request,nav_list=nav_list(),app_name="Lotus Admin",page_name="User")
    details=User.objects.prefetch_related('usergroup_set','employee').get(id=id)
    c['details']=details
    group_apps=GroupApp.objects.filter(group__in=[user_group.group for user_group in details.usergroup_set.all()])
    group_pages=GroupPage.objects.filter(group__in=[user_group.group for user_group in details.usergroup_set.all()])
    c['group_apps']=group_apps
    c['group_pages']=group_pages
    if request.method=="POST":
        print("POST")
        form=UserGroupForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=details
            instance.save()
        else:
            print(form.errors)
        return redirect('lotus_user_employee_details',id)
    elif request.method=="GET":
        print("GET")
        user_group_form=UserGroupForm()
    c['user_group_form']=user_group_form
    return render(request,tftp(subdir="user"),c) 

def lotus_user_student_details(request,id):
    c=cpl(request,nav_list=nav_list(),app_name="Lotus Admin",page_name="User")

    details=User.objects.prefetch_related('usergroup','student').get(id=id)
    c['details']=details
    return render(request,tftp(subdir="user"),c) 


def lotus_user_update(request):
    c=cpl(request,nav_list=nav_list(),app_name="Lotus Admin",page_name="User")
    return render(request,tftp(subdir=lotus_group),c) 


def lotus_user_delete(request,group,app):
    instance=GroupApp.objects.get(id=app)
    instance.delete()
    return redirect('lotus_group_details',group) 

######### END USER GROUPS #########




na_values = ['NA', 'na', 'N/A', 'n/a', '', 'NULL', 'null','nan']

def lotus_importer(request):
    from apps.conductms.models import ConductType,ConductCriteria
    c=cpl(request,app_name="Lotus Admin",page_name="Lotus Importer Page")
    # if request.method=="POST":
    #     form=ExcelImportForm(request.POST,request.FILES)
    #     if form.is_valid():
    #         model=form.cleaned_data['model']
    #         excel_file=request.FILES['file']
    #         data=pd.read_excel(excel_file,engine='openpyxl',sheet_name=model)
    #         for index, row in data.iterrows():
    #             instance=eval(model + "()")
    #             for field in data.columns:
    #                 setattr(instance,field,row[field])
    #             instance.save()    
    #     else:
    #         print(form.errors)
    # elif request.method=="GET":
    #     c['excel_importer_form']=ExcelImportForm()
    return render(request,tftp(subdir="importer"),c) 



def lotus_404(request,violation,message):
    c=cpl(request,app_name="Lotus",page_name="Access Violation")

    return render(request,tftp(subdir="warning"),c) 



def lotus_exception(request):
    c=cpl(request,app_name="Lotus",page_name="Exception Page")

    return render(request,tftp(subdir="warning"),c) 



def lotus_employee_add(request):
    c=cpl(request,nav_list=nav_list(),app_name="Lotus Admin",page_name="User")
    from apps.employeems.forms import EmployeeInitAddForm
    from apps.employeems.models import Employee, EmployeeAddress, EmployeeContactInformation
    from lotus.utils.DioIdGenerator import employee_id_generator
    
    # print(employee_api.get_employee_by_user(request))

    if request.method=="POST":
        form=EmployeeInitAddForm(request.POST)
        if form.is_valid():

            presadd_street=form.cleaned_data['presadd_street']
            presadd_brgy=form.cleaned_data['presadd_brgy']
            presadd_city=form.cleaned_data['presadd_city']
            presadd_prov=form.cleaned_data['presadd_prov']
            presadd_zipcode=form.cleaned_data['presadd_zipcode']

            provadd_street=form.cleaned_data['provadd_street']
            provadd_brgy=form.cleaned_data['provadd_brgy']
            provadd_city=form.cleaned_data['provadd_city']
            provadd_prov=form.cleaned_data['provadd_prov']
            provadd_zipcode=form.cleaned_data['provadd_zipcode']

            

            mobile_no=form.cleaned_data['mobile_no']
            citizenship=form.cleaned_data['citizenship']
            religious_affiliation=form.cleaned_data['religious_affiliation']
            language=form.cleaned_data['language']
            role=form.cleaned_data['role']

            try:
                instance=form.save(commit=False)
                instance.created_by=request.user
                instance.init_log=True
                instance.save()
                print("created employee")
                add_id_no=Employee.objects.get(id=instance.id)
                add_id_no.id_no=employee_id_generator(add_id_no.school.id,1,add_id_no.id)
                add_id_no.save()

                EmployeeAddress.objects.create(
                    employee=instance,
                    address_type_id=1,
                    street=presadd_street,
                    barangay=presadd_brgy,
                    city=presadd_city,
                    province=presadd_prov,
                    zip_code=presadd_zipcode,
                )
                EmployeeAddress.objects.create(
                    employee=instance,
                    address_type_id=2,
                    street=provadd_street,
                    barangay=provadd_brgy,
                    city=provadd_city,
                    province=provadd_prov,
                    zip_code=provadd_zipcode,
                )
                EmployeeContactInformation.objects.create(
                    employee=instance,
                    contact_type_id=1,
                    details=mobile_no,
                    created_by=request.user
                )
                
                print("created employee")
                user=User(username=add_id_no.id_no)
                user.set_password(str(add_id_no.id_no))
                user.save()
                
                user_group_role=Group.objects.get(id=role.id)
                add_user_to_group=UserGroup(user_id=user.id, group=user_group_role,created_by=request.user)
                add_user_to_group.save()

                add_user_to_employee=Employee.objects.get(id=instance.id)
                add_user_to_employee.user=user
                add_user_to_employee.save()

            except Exception as e:
                print(str(e))
            return redirect('employeems_employee_details',instance.id)
        else:
            print(form.errors)

    elif request.method=="GET":
        form=EmployeeInitAddForm()
    c['form']=form
    return render(request,tftp(subdir="employee"),c) 
