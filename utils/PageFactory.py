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
    user_group=get_user_group(user)
    group_apps=get_group_apps(user_group.group)
    group_pages=get_group_pages(user_group.group)
    return False


def extract_keys(nav_list, to_remain):
    remaining_dict = {}

    # Extract paths from to_remain queryset
    paths_to_remain = {item.page.path for item in to_remain}

    # Filter nav_list based on paths_to_remain
    for key, value in nav_list.items():
        if value.get("pathname") in paths_to_remain:
            remaining_dict[key] = value

    return remaining_dict


def create_page_list(request=False,nav_list=False,operation="",page_name=False,app_name=False):
    clu_instance=clu(request.user.id)
    user_group=get_user_group(request.user)

    # user_apps=get_group_apps(group=user_group)
    # user_pages=get_group_pages(group=user_group)
    
    # for apps in user_apps:
    #     print(f"user_apps: {apps.app}")
    # for pages in user_pages:
    #     print(f"user_pages: {pages.page}")
    c={}
  
    perm_nav_list={}
    lts_page_name={}
    if not page_name:
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        subdir=str(calframe[1][3])
        parse_subdir=parse_to_page_info(subdir)
        lts_page_name=create_page_name(parse_subdir)
    elif page_name:
        lts_page_name=page_name        
    if bool(nav_list):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        subdir=str(calframe[1][3])
        print("START perm_nav_list")
        perm_nav_list=extract_keys(nav_list, get_group_pages(user_group))
        # perm_nav_list = _perm_nav_list if _perm_nav_list is not None else {}
        print("END perm_nav_list")
        
        if bool(nav_list.get(subdir,{})) == True:
            nav_list[subdir]['state']='active'

    if operation and operation[0] == '-':

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
        

    return {'nav_list':perm_nav_list,
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
        print(dir[0]+ds+tdn.pages+ds+calframe[1][3]+tdn.html)
        print(dir[0])
        print(calframe[1][3].split("_")[-1])

        print(tdn.pages)
        return dir[0]+ds+tdn.pages+ds+calframe[1][3]+tdn.html
    elif subdir:
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        dir=str(calframe[1][3]).split(_split, 1)
        print(dir[0]+ds+tdn.pages+ds+subdir+ds+calframe[1][3]+tdn.html)
        print(dir[0])
        print(calframe[1][3].split("_")[-1])
        print(tdn.pages)
        return dir[0]+ds+tdn.pages+ds+subdir+ds+calframe[1][3]+tdn.html
    else:
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        dir=str(calframe[1][3]).split(_split, 1)
        print(parent+ds+dir[0]+ds+tdn.pages+ds+calframe[1][3]+tdn.html)
        print(dir[0])
        print(calframe[1][3].split("_")[-1])
        print(tdn.pages)
        return parent+ds+dir[0]+ds+tdn.pages+ds+calframe[1][3]+tdn.html
    
    
    

def caller_to_path():
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)
    dir=str(calframe[1][3]).split(_split, 1)
    print(dir[0]+ds+tdn.pages+ds+calframe[1][3]+tdn.html)
    print(dir[0])
    print(calframe[1][3].split(_split)[-1])
    print("this")
    print(calframe[1][3].split(_split)[1:-1])
    print('that')
    print(tdn.pages)
    print(dir[0]+ds+tdn.pages+ds+calframe[1][3].split(_split)[1:-1][0]+ds+calframe[1][3].split(_split)[-1]+tdn.html)
    return dir[0]+ds+tdn.pages+ds+calframe[1][3].split(_split)[1:-1][0]+ds+calframe[1][3].split(_split)[-1]+tdn.html
