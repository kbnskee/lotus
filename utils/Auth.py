from django.shortcuts import redirect
from lotus.sessions.session import USER_APPS, USER_PAGES, USER_DETAILS

from lotus.models import (
    User,
    UserGroup,
    GroupApp,
    GroupPage

)


def sentry(function):
    def router(request, *args,**kwargs):
        view=function.__name__
        app=view.split("_",1)[0]
        page=view
        user=request.user


        if str(user)=="AnonymousUser":
            return redirect('loginms_login')
        
        if request.user.is_authenticated:
            user_instance=User.objects.get(id=request.user.id)
            user_group=user_instance.usergroup_set.all()


            if str(view)=='loginms_login' or str(view)=='loginms_register' or str(view)=='loginms_forgot_password':
                return redirect('homems_home')                    
            else:
                if app in USER_APPS:
                    print(page)
                    if page in USER_PAGES:
                        print(page)
                        return function(request,*args,**kwargs)
                    else:
                        return redirect(
                            'lotus_404',
                            'Page Access Error',
                            'You do not have access to this page. If you belive you should have access ti this page, please contac the IT Administrators'
                        )
                else:
                    return redirect(
                        'lotus_404',
                        'App Access Error',
                        'You do not have access to this app. If you belive you should have access ti this page, please contac the IT Administrators'
                    )
        else:
            return redirect('loginms_login')
    return router


def sentry_previous_version_0_0_1(function):
    def router(request, *args,**kwargs):
        view=function.__name__
        app=view.split("_",1)[0]
        page=view
        user=request.user

        if str(user)=="AnonymousUser":
            return redirect('loginms_login')
        
        if request.user.is_authenticated:
            user_instance=User.objects.get(id=request.user.id)
            user_group=user_instance.usergroup_set.all()


            if str(view)=='loginms_login' or str(view)=='loginms_register' or str(view)=='loginms_forgot_password':
                return redirect('homems_home')                    
            else:
                if app in USER_APPS:
                    print(page)
                    if page in USER_PAGES:
                        print(page)
                        return function(request,*args,**kwargs)
                    else:
                        return redirect(
                            'lotus_404',
                            'Page Access Error',
                            'You do not have access to this page. If you belive you should have access ti this page, please contac the IT Administrators'
                        )
                else:
                    return redirect(
                        'lotus_404',
                        'App Access Error',
                        'You do not have access to this app. If you belive you should have access ti this page, please contac the IT Administrators'
                    )
        else:
            return redirect('loginms_login')
    return router