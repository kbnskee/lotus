from collections import defaultdict

from lotus.models import User

from apps.employeems.models import Employee

USER_APPS=['homems']
USER_PAGES=['homems_home','homems_profile','homems_change_password','homems_logout']
USER_DETAILS={}

def user_access(req):
    user_instance=User.objects.get(id=req.user.id)
    exist=Employee.objects.filter(user=user_instance).exists()
    if exist:
        USER=Employee.objects.get(user=user_instance)
        print(USER.first_name)
        USER_DETAILS["first_name"]=str(USER.first_name)
        USER_DETAILS["middle_name"]=str(USER.middle_name)
        USER_DETAILS["last_name"]=str(USER.last_name)
        print(USER_DETAILS)
        
        print(f"USER : {USER_DETAILS}")
        user_group=user_instance.usergroup_set.all()
        for list_user_group in user_group:
            print(f"user_group: {list_user_group.group}")
            for apps in list_user_group.group.appgroup_set.all():
                USER_APPS.append(apps.app.name)
                print(USER_APPS)
            for pages in list_user_group.group.pagegroup_set.all():
                USER_PAGES.append(pages.page.name)
                print(USER_PAGES)
