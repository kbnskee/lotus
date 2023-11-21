from lotus.models import User, App, Page, Group, GroupApp, GroupPage, UserGroup


def get_user_group(user): 
    _exists=UserGroup.objects.filter(user=user).exists()
    return UserGroup.objects.get(user=user).group if _exists else "UserGroup Empty"

def get_group_apps(group): 
    _exists=GroupApp.objects.filter(group=group).exists()
    return GroupApp.objects.filter(group=group) if _exists else "UserGroup Empty"

def get_group_pages(group): 
    _exists=GroupPage.objects.filter(group=group).exists()
    return GroupPage.objects.filter(group=group) if _exists else "UserGroup Empty"