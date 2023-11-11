from lotus.models import User, App, Page, Group, GroupApp, GroupPage, UserGroup


get_user_group = lambda user: UserGroup.objects.get(user=user)

get_group_apps = lambda group: GroupApp.objects.filter(group=group)

get_group_pages = lambda group: GroupPage.objects.filter(group=group)