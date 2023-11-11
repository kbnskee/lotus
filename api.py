from lotus.models import User, App, Page, Group, GroupApp, GroupPage, UserGroup


def get_user_group(user): 
    exists=UserGroup.objects.filter(user=user).exists()
    UserGroup.objects.get(user=user) if exists else "UserGroup Empty"

def get_group_apps(group): 
    exists=GroupApp.objects.filter(group=group).exists()
    GroupApp.objects.filter(group=group) if exists else "UserGroup Empty"

def get_group_pages(group): 
    exists=GroupPage.objects.filter(group=group).exists()
    GroupPage.objects.filter(group=group) if exists else "UserGroup Empty"