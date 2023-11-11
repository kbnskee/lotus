import inspect

from django.urls import reverse

from lotus.utils import TemplateDirectoryNames as tdn

from lotus.models import User

from apps.common.views import common_logged_user as clu

from lotus.sessions.session import USER_APPS, USER_PAGES, USER_DETAILS

from lotus.api import (
    get_user_group,
    get_group_apps,
    get_group_pages
)


ds="/"
_split="_"

def lookup_logged_user(user):
    
    return False


def parse_to_page_info(string):
    list=string.split("_")
    app=list[0]
    operation=list[-1]
    if len(list) > 2:
        model=' '.join(list[1:-1])
    else:
        model=[]
    page_info = {
        'app':app, 
        'model': model, 
        'operation': operation
    }
    return page_info


def create_page_name(page_info):
    page_name = page_info['operation'].capitalize() + " "+ page_info['model'].capitalize()
    return page_name




def get_app_pages_by_user(user):
    payload={}
    # user_group=get_user_group(user)
    # group_apps=get_group_apps(user_group.group)
    # group_pages=get_group_pages(user_group.group)
    return False




def create_page_list(request=False,nav_list=False,operation="",page_name=False,app_name=False):
    clu_instance=clu(request.user.id)
    # user_group=get_user_group(request.user)
    # user_apps=get_group_apps(group=user_group.group)
    # user_pages=get_group_pages(group=user_group.group)
    # print(f"user_group: {user_group}")
    
    # for apps in user_apps:
        # print(f"user_apps: {apps.app}")
    # for pages in user_pages:
        # print(f"user_pages: {pages.page}")
    c={}
    lts_page_name={}
    if not page_name:
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        subdir=str(calframe[1][3])
        parse_subdir=parse_to_page_info(subdir)
        print(parse_subdir)
        lts_page_name=create_page_name(parse_subdir)
    elif page_name:
        lts_page_name=page_name        
    if bool(nav_list):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        subdir=str(calframe[1][3])

        
        if bool(nav_list.get(subdir,{})) == True:
            nav_list[subdir]['state']='active'
            print(nav_list[subdir]['state'])

    if operation and operation[0] == '-':
        print("Pass")

        if 'c' in operation:
            function_split=subdir.rsplit('_',1)
            function_operation_add=reverse(str(function_split[0])+"_add")
            c['add']=function_operation_add
        if 'd' in operation:
            function_split=subdir.rsplit('_',1)
            function_operation_delete=reverse(str(function_split[0])+"_delete")
            c['delete']=function_operation_delete
        if 'u' in operation:
            function_split=subdir.rsplit('_',1)
            function_operation_update=reverse(str(function_split[0])+"_update")
            c['update']=function_operation_update
        if 'r' in operation:
            function_split=subdir.rsplit('_',1)
            function_operation_details=(str(function_split[0])+"_details")
            c['details']=function_operation_details 
        if 'l' in operation:
            function_split=subdir.rsplit('_',1)
            function_operation_details=(str(function_split[0])+"_list")
            c['list']=function_operation_details             
        

    return {'nav_list':nav_list,
            'page':{'name':lts_page_name,},
            'page_list':{'page_name':page_name,'app_name':app_name},
            'user_apps':USER_APPS,
            'user_pages':USER_PAGES,
            'function_operation':c,
            'lotus_dmo':c,
            'user_details':clu_instance}


def this_func_to_string():
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe,2)
    return calframe[1][3].replace('_',' ')
    

def this_func_to_path(parent=False,subdir=False):
    if not parent and not subdir:
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        dir=str(calframe[1][3]).split(_split, 1)
        return dir[0]+ds+tdn.pages+ds+calframe[1][3]+tdn.html
    elif subdir:
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        dir=str(calframe[1][3]).split(_split, 1)
        return dir[0]+ds+tdn.pages+ds+subdir+ds+calframe[1][3]+tdn.html
    else:
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        dir=str(calframe[1][3]).split(_split, 1)
        return parent+ds+dir[0]+ds+tdn.pages+ds+calframe[1][3]+tdn.html
        

